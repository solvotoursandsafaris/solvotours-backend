# Generated by Django 5.0.2 on 2025-03-20 08:29

import safaris.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('safaris', '0006_aboutpage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutpage',
            name='image',
            field=models.ImageField(null=True, upload_to=safaris.models.about_image_path),
        ),
    ]
