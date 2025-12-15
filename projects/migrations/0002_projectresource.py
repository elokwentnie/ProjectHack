# Generated manually

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectResource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Display name for the resource', max_length=200)),
                ('description', models.TextField(blank=True, help_text='Brief description of what this resource contains')),
                ('resource_type', models.CharField(choices=[('csv', 'CSV File'), ('json', 'JSON File'), ('txt', 'Text File'), ('zip', 'ZIP Archive'), ('other', 'Other')], default='csv', max_length=10)),
                ('file_path', models.CharField(help_text='Path to the file in static/files/ directory', max_length=500)),
                ('file_size', models.CharField(blank=True, help_text="File size (e.g., '2.5 MB')", max_length=20)),
                ('order', models.IntegerField(default=0, help_text='Display order')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resources', to='projects.project')),
            ],
            options={
                'ordering': ['project', 'order', 'name'],
            },
        ),
        migrations.AlterField(
            model_name='project',
            name='track',
            field=models.CharField(choices=[('frontend', 'Frontend Development'), ('backend', 'Backend Development'), ('fullstack', 'Full-Stack Development'), ('python', 'Python'), ('react', 'React'), ('nodejs', 'Node.js')], max_length=20),
        ),
    ]

