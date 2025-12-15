from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, FileResponse, Http404
from django.views.decorators.http import require_http_methods
from django.utils import timezone
from django.contrib import messages
from django.conf import settings
import uuid
import os
from .models import Project, ProjectStep, ProjectResource, UserSession, UserProfile
from .generator import ProjectGenerator


def home(request):
    """Homepage - project selection with personalized recommendations"""
    # Get or create session ID
    session_id = request.session.get('session_id')
    if not session_id:
        session_id = str(uuid.uuid4())
        request.session['session_id'] = session_id
    
    # Check if user has completed onboarding
    # Always check fresh from database - don't rely on cached values
    onboarding_completed = False
    recommended_projects = []
    user_profile = None
    
    try:
        user_profile = UserProfile.objects.get(session_id=session_id)
        # Explicitly check the onboarding_completed flag - must be True (not just truthy)
        onboarding_completed = user_profile.onboarding_completed is True
        # Also verify that they actually have some preferences set
        if onboarding_completed:
            # Double-check: if they have no preferences, treat as incomplete
            has_preferences = (
                user_profile.experience_level or 
                user_profile.preferred_tracks or 
                user_profile.preferred_difficulty or
                user_profile.interests_keywords
            )
            if not has_preferences:
                # Mark as incomplete if no preferences exist
                onboarding_completed = False
                user_profile.onboarding_completed = False
                user_profile.save()
            else:
                recommended_projects = user_profile.get_recommended_projects(limit=6)
    except UserProfile.DoesNotExist:
        # No profile exists - definitely not completed
        onboarding_completed = False
        recommended_projects = []
        user_profile = None
    
    # If onboarding not completed, redirect to onboarding
    if not onboarding_completed:
        return redirect('projects:onboarding_start')
    
    # Get unique tracks and difficulties
    tracks = Project.TRACK_CHOICES
    difficulties = Project.DIFFICULTY_CHOICES
    timeframes = ProjectStep.TIMEFRAME_CHOICES
    
    # Get projects grouped by track and difficulty (exclude generated projects from main view)
    projects_by_track = {}
    total_projects = 0
    for track_code, track_name in tracks:
        projects_by_track[track_code] = {
            'name': track_name,
            'projects': {}
        }
        for diff_code, diff_name in difficulties:
            projects = Project.objects.filter(track=track_code, difficulty=diff_code, is_generated=False)
            if projects.exists():
                projects_by_track[track_code]['projects'][diff_code] = {
                    'name': diff_name,
                    'projects': projects
                }
                total_projects += projects.count()
    
    # Check if any projects have steps
    projects_with_steps = Project.objects.filter(steps__isnull=False, is_generated=False).distinct().count()
    
    context = {
        'tracks': tracks,
        'difficulties': difficulties,
        'timeframes': timeframes,
        'projects_by_track': projects_by_track,
        'total_projects': total_projects,
        'projects_with_steps': projects_with_steps,
        'recommended_projects': recommended_projects,
        'user_profile': user_profile,
    }
    return render(request, 'projects/home.html', context)


def generate_project(request):
    """Generate a custom project based on user preferences"""
    if request.method == 'POST':
        try:
            track = request.POST.get('track')
            difficulty = request.POST.get('difficulty')
            timeframe = request.POST.get('timeframe')
            keywords = request.POST.get('keywords', '').strip()
            interests = request.POST.get('interests', '').strip()
            
            # Validate inputs
            if not track or track not in dict(Project.TRACK_CHOICES):
                messages.error(request, 'Please select a valid track.')
                return redirect('projects:generate_project')
            
            if not difficulty or difficulty not in dict(Project.DIFFICULTY_CHOICES):
                messages.error(request, 'Please select a valid difficulty level.')
                return redirect('projects:generate_project')
            
            if not timeframe or timeframe not in dict(ProjectStep.TIMEFRAME_CHOICES):
                messages.error(request, 'Please select a valid timeframe.')
                return redirect('projects:generate_project')
            
            # Parse keywords and interests
            keyword_list = [k.strip() for k in keywords.split(',') if k.strip()] if keywords else []
            interest_list = [i.strip() for i in interests.split(',') if i.strip()] if interests else []
            
            # Generate project
            generator = ProjectGenerator()
            project = generator.generate_project(
                track=track,
                difficulty=difficulty,
                timeframe=timeframe,
                keywords=keyword_list,
                interests=interest_list
            )
            
            messages.success(request, f'Project "{project.title}" generated successfully!')
            return redirect('projects:project_overview', project_id=project.id)
        
        except Exception as e:
            messages.error(request, f'Error generating project: {str(e)}. Please try again.')
            return redirect('projects:generate_project')
    
    # GET request - show form
    context = {
        'tracks': Project.TRACK_CHOICES,
        'difficulties': Project.DIFFICULTY_CHOICES,
        'timeframes': ProjectStep.TIMEFRAME_CHOICES,
        'sample_keywords': ProjectGenerator.KEYWORDS[:10],  # Show first 10 as examples
    }
    return render(request, 'projects/generate_project.html', context)


def project_overview(request, project_id):
    """Show project overview and allow user to start"""
    project = get_object_or_404(Project, id=project_id)
    timeframes = ProjectStep.TIMEFRAME_CHOICES
    
    # Get available timeframes for this project
    try:
        # Get distinct timeframes that have steps - use set to ensure uniqueness
        available_timeframes_raw = project.steps.values_list('timeframe', flat=True)
        # Convert to set to remove duplicates, then back to sorted list
        available_timeframes = sorted(set(available_timeframes_raw)) if available_timeframes_raw else []
    except Exception as e:
        # If there's a database error, show helpful message
        messages.error(request, f'Database error: {str(e)}. Please run migrations: python3 manage.py makemigrations && python3 manage.py migrate')
        available_timeframes = []
    
    # If no steps exist, show a message
    if not available_timeframes:
        total_steps = project.steps.count()
        if total_steps == 0:
            messages.warning(request, 'This project does not have any steps configured yet. Please run: python3 manage.py load_sample_projects')
        else:
            messages.warning(request, f'This project has {total_steps} steps but they may not be properly configured. Please reload projects.')
    
    # Filter timeframes to only show those with steps
    # Convert to set for faster lookup
    available_set = set(available_timeframes)
    filtered_timeframes = [tf for tf in timeframes if tf[0] in available_set]
    
    context = {
        'project': project,
        'timeframes': filtered_timeframes,
        'has_steps': bool(available_timeframes),
        'available_timeframes': available_timeframes,  # For debugging
    }
    return render(request, 'projects/project_overview.html', context)


def start_project(request, project_id):
    """Start a new project session"""
    if request.method == 'POST':
        try:
            project = get_object_or_404(Project, id=project_id)
            timeframe = request.POST.get('timeframe')
            
            if not timeframe:
                messages.error(request, 'Please select a timeframe.')
                return redirect('projects:project_overview', project_id=project_id)
            
            if timeframe not in dict(ProjectStep.TIMEFRAME_CHOICES):
                messages.error(request, 'Invalid timeframe selected.')
                return redirect('projects:project_overview', project_id=project_id)
            
            # Check if project has steps for this timeframe
            steps_count = project.steps.filter(timeframe=timeframe).count()
            if steps_count == 0:
                messages.error(request, f'This project does not have steps configured for {timeframe} timeframe.')
                return redirect('projects:project_overview', project_id=project_id)
            
            # Generate or get session ID
            session_id = request.session.get('session_id')
            if not session_id:
                session_id = str(uuid.uuid4())
                request.session['session_id'] = session_id
            
            # Create or get user session
            # Handle case where multiple sessions might exist
            # First, delete any existing incomplete sessions for this project/timeframe
            UserSession.objects.filter(
                session_id=session_id,
                project=project,
                selected_timeframe=timeframe,
                completed=False
            ).delete()
            
            # Create new session
            user_session = UserSession.objects.create(
                session_id=session_id,
                project=project,
                selected_timeframe=timeframe,
                start_time=timezone.now(),
                current_step=1,
                completed_steps=[],
                completed=False
            )
            
            return redirect('projects:project_step', session_id=user_session.id)
        
        except Exception as e:
            messages.error(request, f'An error occurred: {str(e)}. Please try again.')
            return redirect('projects:project_overview', project_id=project_id)
    
    return redirect('projects:home')


def project_step(request, session_id):
    """Show current step of the project"""
    user_session = get_object_or_404(UserSession, id=session_id)
    
    # Verify session belongs to user
    if request.session.get('session_id') != user_session.session_id:
        messages.error(request, 'Invalid session.')
        return redirect('projects:home')
    
    # Get current step
    steps = ProjectStep.objects.filter(
        project=user_session.project,
        timeframe=user_session.selected_timeframe
    ).order_by('step_number')
    
    if not steps.exists():
        messages.error(request, 'No steps available for this project.')
        return redirect('projects:home')
    
    # Get current step
    current_step_obj = steps.filter(step_number=user_session.current_step).first()
    
    if not current_step_obj:
        # Project completed
        return redirect('projects:project_summary', session_id=session_id)
    
    # Get all steps for progress
    all_steps = list(steps)
    current_index = user_session.current_step - 1
    
    # Get downloadable resources for this project
    # Use try-except in case ProjectResource table doesn't exist (migrations not run)
    try:
        resources = list(user_session.project.resources.all())
    except Exception as e:
        # If ProjectResource table doesn't exist yet (migrations not run), return empty
        resources = []
    
    context = {
        'user_session': user_session,
        'current_step': current_step_obj,
        'all_steps': all_steps,
        'current_index': current_index,
        'total_steps': len(all_steps),
        'progress_percentage': user_session.get_progress_percentage(),
        'remaining_seconds': user_session.get_remaining_time(),
        'resources': resources,
    }
    return render(request, 'projects/project_step.html', context)


def complete_step(request, session_id):
    """Mark current step as complete and move to next"""
    if request.method == 'POST':
        user_session = get_object_or_404(UserSession, id=session_id)
        
        # Verify session
        if request.session.get('session_id') != user_session.session_id:
            return JsonResponse({'error': 'Invalid session'}, status=403)
        
        # Mark current step as completed
        if user_session.current_step not in user_session.completed_steps:
            user_session.completed_steps.append(user_session.current_step)
        
        # Move to next step
        total_steps = user_session.get_total_steps()
        if user_session.current_step < total_steps:
            user_session.current_step += 1
        else:
            # All steps completed
            user_session.completed = True
            user_session.completed_at = timezone.now()
        
        user_session.save()
        
        return JsonResponse({
            'success': True,
            'completed': user_session.completed,
            'next_step': user_session.current_step if not user_session.completed else None
        })
    
    return JsonResponse({'error': 'Invalid method'}, status=405)


def project_summary(request, session_id):
    """Show project summary and skills learned"""
    user_session = get_object_or_404(UserSession, id=session_id)
    
    # Verify session
    if request.session.get('session_id') != user_session.session_id:
        messages.error(request, 'Invalid session.')
        return redirect('projects:home')
    
    # Collect all technologies learned
    completed_steps = ProjectStep.objects.filter(
        project=user_session.project,
        timeframe=user_session.selected_timeframe,
        step_number__in=user_session.completed_steps
    ).order_by('step_number')
    
    all_technologies = []
    for step in completed_steps:
        all_technologies.extend(step.technologies)
    
    # Remove duplicates while preserving order
    unique_technologies = list(dict.fromkeys(all_technologies))
    
    # Generate CV-ready summary
    cv_summary = generate_cv_summary(user_session, unique_technologies, completed_steps)
    
    context = {
        'user_session': user_session,
        'technologies': unique_technologies,
        'completed_steps': completed_steps,
        'cv_summary': cv_summary,
    }
    return render(request, 'projects/project_summary.html', context)


def submit_project(request, session_id):
    """Submit GitHub repository link"""
    if request.method == 'POST':
        user_session = get_object_or_404(UserSession, id=session_id)
        
        # Verify session
        if request.session.get('session_id') != user_session.session_id:
            messages.error(request, 'Invalid session.')
            return redirect('home')
        
        github_repo = request.POST.get('github_repo', '').strip()
        
        if github_repo:
            # Basic URL validation
            if github_repo.startswith(('http://', 'https://')):
                user_session.github_repo = github_repo
                user_session.save()
                messages.success(request, 'Thank you for sharing your project!')
            else:
                messages.error(request, 'Please enter a valid URL (starting with http:// or https://)')
        else:
            messages.error(request, 'Please enter a GitHub repository URL')
        
        return redirect('projects:project_summary', session_id=session_id)
    
    return redirect('projects:home')


def generate_cv_summary(user_session, technologies, completed_steps):
    """Generate a CV-ready summary of the project"""
    project = user_session.project
    timeframe_hours = int(user_session.selected_timeframe.replace('h', ''))
    
    summary = {
        'project_title': project.title,
        'description': f"Built a {project.title.lower()} as part of a {timeframe_hours}-hour solo hackathon project.",
        'technologies': technologies,
        'key_achievements': [
            f"Completed {len(completed_steps)} structured development steps",
            f"Implemented project from concept to working MVP in {timeframe_hours} hours",
            "Applied version control best practices with Git and GitHub",
            "Followed step-by-step development methodology",
        ],
        'skills_learned': technologies + [
            "Project planning and time management",
            "End-to-end project development",
            "Git version control",
            "Problem-solving and debugging",
        ],
        'cv_bullet_points': [
            f"Developed {project.title.lower()} using {', '.join(technologies[:3])} and additional technologies",
            f"Completed project in {timeframe_hours}-hour timeframe, demonstrating time management and project planning skills",
            "Implemented project following structured development methodology with {0} distinct steps".format(len(completed_steps)),
            "Utilized Git and GitHub for version control and project documentation",
        ]
    }
    
    return summary


def timer_status(request, session_id):
    """API endpoint to get timer status"""
    user_session = get_object_or_404(UserSession, id=session_id)
    
    # Verify session
    if request.session.get('session_id') != user_session.session_id:
        return JsonResponse({'error': 'Invalid session'}, status=403)
    
    remaining_seconds = user_session.get_remaining_time()
    is_expired = remaining_seconds == 0
    
    return JsonResponse({
        'remaining_seconds': remaining_seconds,
        'is_expired': is_expired,
        'progress': user_session.get_progress_percentage(),
        'current_step': user_session.current_step,
        'total_steps': user_session.get_total_steps(),
    })


def download_resource(request, resource_id):
    """Download a project resource file"""
    resource = get_object_or_404(ProjectResource, id=resource_id)
    
    # Build file path - file_path should be relative to static/files/
    if resource.file_path.startswith('/'):
        file_path = os.path.join(settings.BASE_DIR, 'static', 'files', resource.file_path.lstrip('/'))
    else:
        file_path = os.path.join(settings.BASE_DIR, 'static', 'files', resource.file_path)
    
    if not os.path.exists(file_path):
        raise Http404(f"File not found: {file_path}")
    
    # Determine content type
    content_types = {
        'csv': 'text/csv',
        'json': 'application/json',
        'txt': 'text/plain',
        'zip': 'application/zip',
    }
    content_type = content_types.get(resource.resource_type, 'application/octet-stream')
    
    # Get filename from path
    filename = os.path.basename(resource.file_path)
    
    # Return file response
    try:
        file_handle = open(file_path, 'rb')
        response = FileResponse(file_handle, content_type=content_type)
        response['Content-Disposition'] = f'attachment; filename="{filename}"'
        return response
    except Exception as e:
        raise Http404(f"Error opening file: {str(e)}")


# ========== ONBOARDING FLOW ==========

def onboarding_start(request):
    """Start onboarding flow - Question 1: Experience Level"""
    session_id = request.session.get('session_id')
    if not session_id:
        session_id = str(uuid.uuid4())
        request.session['session_id'] = session_id
    
    # Check if user wants to reset onboarding (from query parameter)
    reset = request.GET.get('reset', 'false').lower() == 'true'
    
    # Get or create user profile
    try:
        user_profile = UserProfile.objects.get(session_id=session_id)
        # If reset requested, clear onboarding status
        if reset:
            user_profile.onboarding_completed = False
            user_profile.experience_level = ''
            user_profile.interested_technologies = []
            user_profile.preferred_tracks = []
            user_profile.preferred_difficulty = ''
            user_profile.preferred_timeframe = ''
            user_profile.interests_keywords = []
            user_profile.save()
    except UserProfile.DoesNotExist:
        user_profile = UserProfile.objects.create(session_id=session_id)
    
    if request.method == 'POST':
        experience_level = request.POST.get('experience_level')
        if experience_level:
            user_profile.experience_level = experience_level
            user_profile.save()
            return redirect('projects:onboarding_technologies')
    
    context = {
        'experience_levels': UserProfile.EXPERIENCE_LEVELS,
        'current_step': 1,
        'total_steps': 4,
    }
    return render(request, 'projects/onboarding/experience.html', context)


def onboarding_technologies(request):
    """Onboarding Question 2: Technologies of Interest"""
    session_id = request.session.get('session_id')
    if not session_id:
        return redirect('projects:onboarding_start')
    
    try:
        user_profile = UserProfile.objects.get(session_id=session_id)
    except UserProfile.DoesNotExist:
        return redirect('projects:onboarding_start')
    
    # Available technologies based on tracks
    all_technologies = {
        'frontend': ['HTML', 'CSS', 'JavaScript', 'React', 'Vue.js', 'Angular', 'TypeScript', 'Tailwind CSS', 'SASS'],
        'backend': ['Python', 'Django', 'Flask', 'Node.js', 'Express', 'REST API', 'GraphQL', 'PostgreSQL', 'MongoDB'],
        'fullstack': ['React', 'Node.js', 'Express', 'MongoDB', 'PostgreSQL', 'TypeScript', 'Next.js'],
        'python': ['Python', 'Django', 'Flask', 'Pandas', 'NumPy', 'Matplotlib', 'FastAPI'],
        'react': ['React', 'JavaScript', 'TypeScript', 'Redux', 'React Router', 'Next.js'],
        'nodejs': ['Node.js', 'Express', 'JavaScript', 'TypeScript', 'MongoDB', 'REST API'],
    }
    
    if request.method == 'POST':
        selected_technologies = request.POST.getlist('technologies')
        if selected_technologies:
            user_profile.interested_technologies = selected_technologies
            user_profile.save()
            return redirect('projects:onboarding_tracks')
    
    context = {
        'all_technologies': all_technologies,
        'current_step': 2,
        'total_steps': 4,
    }
    return render(request, 'projects/onboarding/technologies.html', context)


def onboarding_tracks(request):
    """Onboarding Question 3: Preferred Tracks"""
    session_id = request.session.get('session_id')
    if not session_id:
        return redirect('projects:onboarding_start')
    
    try:
        user_profile = UserProfile.objects.get(session_id=session_id)
    except UserProfile.DoesNotExist:
        return redirect('projects:onboarding_start')
    
    if request.method == 'POST':
        preferred_tracks = request.POST.getlist('tracks')
        preferred_difficulty = request.POST.get('difficulty', '')
        preferred_timeframe = request.POST.get('timeframe', '')
        
        if preferred_tracks:
            user_profile.preferred_tracks = preferred_tracks
        if preferred_difficulty:
            user_profile.preferred_difficulty = preferred_difficulty
        if preferred_timeframe:
            user_profile.preferred_timeframe = preferred_timeframe
        user_profile.save()
        return redirect('projects:onboarding_interests')
    
    context = {
        'tracks': Project.TRACK_CHOICES,
        'difficulties': Project.DIFFICULTY_CHOICES,
        'timeframes': ProjectStep.TIMEFRAME_CHOICES,
        'current_step': 3,
        'total_steps': 4,
    }
    return render(request, 'projects/onboarding/tracks.html', context)


def onboarding_interests(request):
    """Onboarding Question 4: Interests/Keywords"""
    session_id = request.session.get('session_id')
    if not session_id:
        return redirect('projects:onboarding_start')
    
    try:
        user_profile = UserProfile.objects.get(session_id=session_id)
    except UserProfile.DoesNotExist:
        return redirect('projects:onboarding_start')
    
    # Sample keywords for suggestions
    sample_keywords = [
        'E-commerce', 'Social Media', 'Blog', 'Dashboard', 'API', 'Mobile App',
        'Data Visualization', 'Automation', 'Game', 'Portfolio', 'Weather',
        'Todo', 'Calculator', 'Chat', 'Music', 'Video', 'Education', 'Health',
        'Finance', 'Travel', 'Food', 'Sports', 'News', 'Shopping'
    ]
    
    if request.method == 'POST':
        interests = request.POST.get('interests', '')
        if interests:
            # Split by comma and clean up
            interest_list = [i.strip() for i in interests.split(',') if i.strip()]
            user_profile.interests_keywords = interest_list
            user_profile.onboarding_completed = True
            user_profile.save()
            return redirect('projects:onboarding_complete')
    
    context = {
        'sample_keywords': sample_keywords,
        'current_step': 4,
        'total_steps': 4,
    }
    return render(request, 'projects/onboarding/interests.html', context)


def onboarding_complete(request):
    """Show recommended projects after onboarding"""
    session_id = request.session.get('session_id')
    if not session_id:
        return redirect('projects:onboarding_start')
    
    try:
        user_profile = UserProfile.objects.get(session_id=session_id)
    except UserProfile.DoesNotExist:
        return redirect('projects:onboarding_start')
    
    # Get recommended projects
    recommended_projects = user_profile.get_recommended_projects(limit=6)
    
    # Also get some alternative projects
    all_projects = Project.objects.filter(is_generated=False).exclude(
        id__in=[p.id for p in recommended_projects]
    )[:6]
    
    context = {
        'user_profile': user_profile,
        'recommended_projects': recommended_projects,
        'alternative_projects': all_projects,
    }
    return render(request, 'projects/onboarding/complete.html', context)

