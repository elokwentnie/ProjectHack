# Generated manually

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_projectresource'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_id', models.CharField(db_index=True, max_length=100, unique=True)),
                ('experience_level', models.CharField(blank=True, choices=[('beginner', 'Complete Beginner'), ('some_experience', 'Some Experience'), ('intermediate', 'Intermediate'), ('advanced', 'Advanced')], max_length=20)),
                ('interested_technologies', models.JSONField(default=list, help_text='List of technologies user is interested in')),
                ('preferred_tracks', models.JSONField(default=list, help_text='List of tracks user prefers')),
                ('preferred_difficulty', models.CharField(blank=True, max_length=20)),
                ('preferred_timeframe', models.CharField(blank=True, max_length=10)),
                ('interests_keywords', models.JSONField(default=list, help_text='Keywords describing user interests')),
                ('onboarding_completed', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-updated_at'],
            },
        ),
    ]

