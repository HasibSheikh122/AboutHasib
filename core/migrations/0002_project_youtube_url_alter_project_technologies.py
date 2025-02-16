# Generated by Django 5.1.4 on 2025-01-04 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='youtube_url',
            field=models.URLField(blank=True, help_text="Add a YouTube URL if there's a demo video.", null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='technologies',
            field=models.CharField(help_text='Comma-separated list of technologies (e.g., Django, React, PostgreSQL)', max_length=200),
        ),
    ]
