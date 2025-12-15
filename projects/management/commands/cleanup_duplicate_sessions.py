from django.core.management.base import BaseCommand
from django.db.models import Count
from projects.models import UserSession


class Command(BaseCommand):
    help = 'Clean up duplicate user sessions'

    def handle(self, *args, **options):
        self.stdout.write('Cleaning up duplicate sessions...')
        
        # Find duplicate sessions (same session_id, project, timeframe, not completed)
        duplicates = UserSession.objects.filter(completed=False).values(
            'session_id', 'project', 'selected_timeframe'
        ).annotate(
            count=Count('id')
        ).filter(count__gt=1)
        
        total_deleted = 0
        for dup in duplicates:
            sessions = UserSession.objects.filter(
                session_id=dup['session_id'],
                project_id=dup['project'],
                selected_timeframe=dup['selected_timeframe'],
                completed=False
            ).order_by('-start_time')
            
            # Keep the most recent one, delete others
            if sessions.count() > 1:
                to_keep = sessions.first()
                to_delete = sessions.exclude(id=to_keep.id)
                count = to_delete.count()
                to_delete.delete()
                total_deleted += count
                self.stdout.write(f'Deleted {count} duplicate session(s) for {to_keep.project.title}')
        
        self.stdout.write(self.style.SUCCESS(f'Successfully cleaned up {total_deleted} duplicate sessions!'))

