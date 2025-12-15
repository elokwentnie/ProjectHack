from django.core.management.base import BaseCommand
from projects.models import UserProfile


class Command(BaseCommand):
    help = 'Reset onboarding for all users or a specific session'

    def add_arguments(self, parser):
        parser.add_argument(
            '--session-id',
            type=str,
            help='Reset onboarding for a specific session ID',
        )
        parser.add_argument(
            '--all',
            action='store_true',
            help='Reset onboarding for all users',
        )

    def handle(self, *args, **options):
        if options['all']:
            # Reset all user profiles
            count = UserProfile.objects.all().count()
            UserProfile.objects.all().delete()
            self.stdout.write(self.style.SUCCESS(f'Successfully deleted {count} user profile(s)!'))
        elif options['session_id']:
            # Reset specific session
            try:
                profile = UserProfile.objects.get(session_id=options['session_id'])
                profile.delete()
                self.stdout.write(self.style.SUCCESS(f'Successfully deleted profile for session {options["session_id"]}'))
            except UserProfile.DoesNotExist:
                self.stdout.write(self.style.WARNING(f'No profile found for session {options["session_id"]}'))
        else:
            # Reset current session (most recent)
            profile = UserProfile.objects.order_by('-updated_at').first()
            if profile:
                session_id = profile.session_id
                profile.delete()
                self.stdout.write(self.style.SUCCESS(f'Successfully deleted most recent profile (session: {session_id[:8]}...)'))
            else:
                self.stdout.write(self.style.WARNING('No user profiles found to delete.'))

