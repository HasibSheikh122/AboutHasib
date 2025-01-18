# Generated by Django 5.1.4 on 2025-01-09 01:15

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_testimonial_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='profile_image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]
