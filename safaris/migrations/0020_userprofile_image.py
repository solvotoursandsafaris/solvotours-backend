# Generated by Django 5.0.2 on 2025-07-15 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('safaris', '0019_destination_local_culture_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_images/'),
        ),
    ]
