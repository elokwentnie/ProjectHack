from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta
from .models import Project, ProjectStep, UserSession


class ProjectModelTest(TestCase):
    """Test Project model"""
    
    def setUp(self):
        self.project = Project.objects.create(
            title='Test Project',
            description='Test description',
            difficulty='beginner',
            track='web_dev'
        )
    
    def test_project_creation(self):
        """Test that a project can be created"""
        self.assertEqual(self.project.title, 'Test Project')
        self.assertEqual(self.project.difficulty, 'beginner')
        self.assertEqual(self.project.track, 'web_dev')
    
    def test_project_str(self):
        """Test project string representation"""
        self.assertEqual(str(self.project), 'Test Project (Beginner)')


class ProjectStepModelTest(TestCase):
    """Test ProjectStep model"""
    
    def setUp(self):
        self.project = Project.objects.create(
            title='Test Project',
            description='Test description',
            difficulty='beginner',
            track='web_dev'
        )
        self.step = ProjectStep.objects.create(
            project=self.project,
            step_number=1,
            title='Test Step',
            description='Test step description',
            technologies=['HTML', 'CSS'],
            estimated_time=60,
            timeframe='6h',
            learning_outcomes='Test learning outcomes'
        )
    
    def test_step_creation(self):
        """Test that a step can be created"""
        self.assertEqual(self.step.project, self.project)
        self.assertEqual(self.step.step_number, 1)
        self.assertEqual(self.step.timeframe, '6h')
        self.assertEqual(self.step.technologies, ['HTML', 'CSS'])
    
    def test_step_str(self):
        """Test step string representation"""
        expected = 'Test Project - Step 1 (6h)'
        self.assertEqual(str(self.step), expected)


class UserSessionModelTest(TestCase):
    """Test UserSession model"""
    
    def setUp(self):
        self.project = Project.objects.create(
            title='Test Project',
            description='Test description',
            difficulty='beginner',
            track='web_dev'
        )
        # Create steps for 6h timeframe
        for i in range(1, 4):
            ProjectStep.objects.create(
                project=self.project,
                step_number=i,
                title=f'Step {i}',
                description=f'Description {i}',
                technologies=['HTML'],
                estimated_time=60,
                timeframe='6h'
            )
        
        self.session = UserSession.objects.create(
            session_id='test-session-123',
            project=self.project,
            selected_timeframe='6h',
            start_time=timezone.now(),
            current_step=1,
            completed_steps=[]
        )
    
    def test_session_creation(self):
        """Test that a session can be created"""
        self.assertEqual(self.session.project, self.project)
        self.assertEqual(self.session.selected_timeframe, '6h')
        self.assertEqual(self.session.current_step, 1)
        self.assertFalse(self.session.completed)
    
    def test_get_total_steps(self):
        """Test getting total steps for timeframe"""
        total = self.session.get_total_steps()
        self.assertEqual(total, 3)
    
    def test_get_progress_percentage(self):
        """Test progress percentage calculation"""
        # No steps completed
        self.assertEqual(self.session.get_progress_percentage(), 0)
        
        # Complete one step
        self.session.completed_steps = [1]
        self.session.save()
        self.assertEqual(self.session.get_progress_percentage(), 33)
        
        # Complete all steps
        self.session.completed_steps = [1, 2, 3]
        self.session.save()
        self.assertEqual(self.session.get_progress_percentage(), 100)
    
    def test_get_remaining_time(self):
        """Test remaining time calculation"""
        # Start time is now, so remaining should be close to 6 hours
        remaining = self.session.get_remaining_time()
        self.assertGreater(remaining, 0)
        self.assertLessEqual(remaining, 6 * 3600)  # 6 hours in seconds
        
        # Test expired session
        self.session.start_time = timezone.now() - timedelta(hours=7)
        self.session.save()
        remaining = self.session.get_remaining_time()
        self.assertEqual(remaining, 0)


class HomeViewTest(TestCase):
    """Test home view"""
    
    def setUp(self):
        self.client = Client()
        self.project = Project.objects.create(
            title='Test Project',
            description='Test description',
            difficulty='beginner',
            track='web_dev'
        )
    
    def test_home_view(self):
        """Test that home page loads"""
        response = self.client.get(reverse('projects:home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Project')
    
    def test_home_view_with_no_projects(self):
        """Test home view with no projects"""
        Project.objects.all().delete()
        response = self.client.get(reverse('projects:home'))
        self.assertEqual(response.status_code, 200)


class ProjectOverviewViewTest(TestCase):
    """Test project overview view"""
    
    def setUp(self):
        self.client = Client()
        self.project = Project.objects.create(
            title='Test Project',
            description='Test description',
            difficulty='beginner',
            track='web_dev'
        )
        ProjectStep.objects.create(
            project=self.project,
            step_number=1,
            title='Step 1',
            description='Description',
            technologies=['HTML'],
            estimated_time=60,
            timeframe='6h'
        )
    
    def test_project_overview_view(self):
        """Test project overview page"""
        response = self.client.get(reverse('projects:project_overview', args=[self.project.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Project')
    
    def test_project_overview_404(self):
        """Test 404 for non-existent project"""
        response = self.client.get(reverse('projects:project_overview', args=[999]))
        self.assertEqual(response.status_code, 404)


class StartProjectViewTest(TestCase):
    """Test start project view"""
    
    def setUp(self):
        self.client = Client()
        self.project = Project.objects.create(
            title='Test Project',
            description='Test description',
            difficulty='beginner',
            track='web_dev'
        )
        ProjectStep.objects.create(
            project=self.project,
            step_number=1,
            title='Step 1',
            description='Description',
            technologies=['HTML'],
            estimated_time=60,
            timeframe='6h'
        )
    
    def test_start_project_post(self):
        """Test starting a project"""
        response = self.client.post(
            reverse('projects:start_project', args=[self.project.id]),
            {'timeframe': '6h'}
        )
        self.assertEqual(response.status_code, 302)  # Redirect
        
        # Check that session was created
        session = UserSession.objects.first()
        self.assertIsNotNone(session)
        self.assertEqual(session.project, self.project)
        self.assertEqual(session.selected_timeframe, '6h')
    
    def test_start_project_invalid_timeframe(self):
        """Test starting project with invalid timeframe"""
        response = self.client.post(
            reverse('projects:start_project', args=[self.project.id]),
            {'timeframe': 'invalid'}
        )
        self.assertEqual(response.status_code, 302)  # Redirect with error
    
    def test_start_project_get(self):
        """Test GET request to start project redirects to home"""
        response = self.client.get(reverse('projects:start_project', args=[self.project.id]))
        self.assertEqual(response.status_code, 302)


class ProjectStepViewTest(TestCase):
    """Test project step view"""
    
    def setUp(self):
        self.client = Client()
        self.project = Project.objects.create(
            title='Test Project',
            description='Test description',
            difficulty='beginner',
            track='web_dev'
        )
        self.step = ProjectStep.objects.create(
            project=self.project,
            step_number=1,
            title='Step 1',
            description='Description',
            technologies=['HTML'],
            estimated_time=60,
            timeframe='6h'
        )
        self.session = UserSession.objects.create(
            session_id='test-session',
            project=self.project,
            selected_timeframe='6h',
            start_time=timezone.now(),
            current_step=1
        )
        # Set session in client
        session = self.client.session
        session['session_id'] = 'test-session'
        session.save()
    
    def test_project_step_view(self):
        """Test viewing a project step"""
        response = self.client.get(reverse('projects:project_step', args=[self.session.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Step 1')
    
    def test_project_step_invalid_session(self):
        """Test accessing step with wrong session"""
        session = self.client.session
        session['session_id'] = 'wrong-session'
        session.save()
        response = self.client.get(reverse('projects:project_step', args=[self.session.id]))
        self.assertEqual(response.status_code, 302)  # Redirect to home
    
    def test_project_step_completed_project(self):
        """Test viewing step when project is completed"""
        self.session.current_step = 10  # Beyond available steps
        self.session.save()
        response = self.client.get(reverse('projects:project_step', args=[self.session.id]))
        self.assertEqual(response.status_code, 302)  # Redirect to summary


class CompleteStepViewTest(TestCase):
    """Test complete step view"""
    
    def setUp(self):
        self.client = Client()
        self.project = Project.objects.create(
            title='Test Project',
            description='Test description',
            difficulty='beginner',
            track='web_dev'
        )
        # Create 2 steps
        for i in range(1, 3):
            ProjectStep.objects.create(
                project=self.project,
                step_number=i,
                title=f'Step {i}',
                description='Description',
                technologies=['HTML'],
                estimated_time=60,
                timeframe='6h'
            )
        self.session = UserSession.objects.create(
            session_id='test-session',
            project=self.project,
            selected_timeframe='6h',
            start_time=timezone.now(),
            current_step=1
        )
        session = self.client.session
        session['session_id'] = 'test-session'
        session.save()
    
    def test_complete_step(self):
        """Test completing a step"""
        response = self.client.post(reverse('projects:complete_step', args=[self.session.id]))
        self.assertEqual(response.status_code, 200)
        
        # Check session was updated
        self.session.refresh_from_db()
        self.assertIn(1, self.session.completed_steps)
        self.assertEqual(self.session.current_step, 2)
        self.assertFalse(self.session.completed)
    
    def test_complete_final_step(self):
        """Test completing the final step"""
        self.session.current_step = 2
        self.session.save()
        
        response = self.client.post(reverse('projects:complete_step', args=[self.session.id]))
        self.assertEqual(response.status_code, 200)
        
        # Check session was completed
        self.session.refresh_from_db()
        self.assertTrue(self.session.completed)
        self.assertIsNotNone(self.session.completed_at)
    
    def test_complete_step_invalid_session(self):
        """Test completing step with wrong session"""
        session = self.client.session
        session['session_id'] = 'wrong-session'
        session.save()
        response = self.client.post(reverse('projects:complete_step', args=[self.session.id]))
        self.assertEqual(response.status_code, 403)
    
    def test_complete_step_get(self):
        """Test GET request to complete step"""
        response = self.client.get(reverse('projects:complete_step', args=[self.session.id]))
        self.assertEqual(response.status_code, 405)  # Method not allowed


class ProjectSummaryViewTest(TestCase):
    """Test project summary view"""
    
    def setUp(self):
        self.client = Client()
        self.project = Project.objects.create(
            title='Test Project',
            description='Test description',
            difficulty='beginner',
            track='web_dev'
        )
        self.step = ProjectStep.objects.create(
            project=self.project,
            step_number=1,
            title='Step 1',
            description='Description',
            technologies=['HTML', 'CSS'],
            estimated_time=60,
            timeframe='6h'
        )
        self.session = UserSession.objects.create(
            session_id='test-session',
            project=self.project,
            selected_timeframe='6h',
            start_time=timezone.now(),
            current_step=2,
            completed_steps=[1],
            completed=True
        )
        session = self.client.session
        session['session_id'] = 'test-session'
        session.save()
    
    def test_project_summary_view(self):
        """Test project summary page"""
        response = self.client.get(reverse('projects:project_summary', args=[self.session.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Project')
        # Check technologies are shown
        self.assertContains(response, 'HTML')
        self.assertContains(response, 'CSS')
    
    def test_project_summary_invalid_session(self):
        """Test summary with wrong session"""
        session = self.client.session
        session['session_id'] = 'wrong-session'
        session.save()
        response = self.client.get(reverse('projects:project_summary', args=[self.session.id]))
        self.assertEqual(response.status_code, 302)  # Redirect to home


class SubmitProjectViewTest(TestCase):
    """Test submit project view"""
    
    def setUp(self):
        self.client = Client()
        self.project = Project.objects.create(
            title='Test Project',
            description='Test description',
            difficulty='beginner',
            track='web_dev'
        )
        self.session = UserSession.objects.create(
            session_id='test-session',
            project=self.project,
            selected_timeframe='6h',
            start_time=timezone.now()
        )
        session = self.client.session
        session['session_id'] = 'test-session'
        session.save()
    
    def test_submit_project_valid_url(self):
        """Test submitting a valid GitHub URL"""
        response = self.client.post(
            reverse('projects:submit_project', args=[self.session.id]),
            {'github_repo': 'https://github.com/user/repo'}
        )
        self.assertEqual(response.status_code, 302)  # Redirect
        
        self.session.refresh_from_db()
        self.assertEqual(self.session.github_repo, 'https://github.com/user/repo')
    
    def test_submit_project_invalid_url(self):
        """Test submitting an invalid URL"""
        response = self.client.post(
            reverse('projects:submit_project', args=[self.session.id]),
            {'github_repo': 'not-a-url'}
        )
        self.assertEqual(response.status_code, 302)  # Redirect with error
    
    def test_submit_project_empty_url(self):
        """Test submitting empty URL"""
        response = self.client.post(
            reverse('projects:submit_project', args=[self.session.id]),
            {'github_repo': ''}
        )
        self.assertEqual(response.status_code, 302)  # Redirect with error


class TimerStatusViewTest(TestCase):
    """Test timer status API view"""
    
    def setUp(self):
        self.client = Client()
        self.project = Project.objects.create(
            title='Test Project',
            description='Test description',
            difficulty='beginner',
            track='web_dev'
        )
        ProjectStep.objects.create(
            project=self.project,
            step_number=1,
            title='Step 1',
            description='Description',
            technologies=['HTML'],
            estimated_time=60,
            timeframe='6h'
        )
        self.session = UserSession.objects.create(
            session_id='test-session',
            project=self.project,
            selected_timeframe='6h',
            start_time=timezone.now(),
            current_step=1
        )
        session = self.client.session
        session['session_id'] = 'test-session'
        session.save()
    
    def test_timer_status(self):
        """Test timer status API"""
        response = self.client.get(reverse('projects:timer_status', args=[self.session.id]))
        self.assertEqual(response.status_code, 200)
        
        data = response.json()
        self.assertIn('remaining_seconds', data)
        self.assertIn('is_expired', data)
        self.assertIn('progress', data)
        self.assertIn('current_step', data)
        self.assertIn('total_steps', data)
        self.assertGreater(data['remaining_seconds'], 0)
        self.assertFalse(data['is_expired'])
    
    def test_timer_status_invalid_session(self):
        """Test timer status with wrong session"""
        session = self.client.session
        session['session_id'] = 'wrong-session'
        session.save()
        response = self.client.get(reverse('projects:timer_status', args=[self.session.id]))
        self.assertEqual(response.status_code, 403)

