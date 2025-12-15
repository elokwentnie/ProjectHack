from django.core.management.base import BaseCommand
from projects.models import Project, ProjectStep


class Command(BaseCommand):
    help = 'Check which projects have steps for which timeframes'

    def handle(self, *args, **options):
        self.stdout.write('Checking project steps...\n')
        
        projects = Project.objects.all()
        
        if not projects.exists():
            self.stdout.write(self.style.WARNING('No projects found. Run: python3 manage.py load_sample_projects'))
            return
        
        for project in projects:
            self.stdout.write(f'\n{project.title} ({project.get_track_display()}, {project.get_difficulty_display()})')
            
            # Get timeframes with steps
            timeframes = ProjectStep.objects.filter(project=project).values_list('timeframe', flat=True).distinct()
            
            if not timeframes:
                self.stdout.write(self.style.ERROR('  ❌ No steps configured'))
            else:
                self.stdout.write(self.style.SUCCESS(f'  ✅ Available timeframes: {", ".join(sorted(timeframes))}'))
                
                # Show step counts per timeframe
                for tf in sorted(timeframes):
                    count = ProjectStep.objects.filter(project=project, timeframe=tf).count()
                    self.stdout.write(f'     - {tf}: {count} steps')
        
        self.stdout.write('\n' + '='*50)
        total_projects = projects.count()
        total_steps = ProjectStep.objects.count()
        self.stdout.write(f'Total: {total_projects} projects, {total_steps} steps')

