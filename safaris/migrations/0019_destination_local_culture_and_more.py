# Generated by Django 5.0.2 on 2025-06-17 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('safaris', '0018_faq_blog_gallery'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='local_culture',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='destination',
            name='weather_information',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='destination',
            name='wildlife_information',
            field=models.TextField(blank=True, null=True),
        ),
    ]
