# Generated by Django 4.2.16 on 2024-12-14 07:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountuser',
            name='following',
            field=models.ManyToManyField(blank=True, related_name='is_following', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='accountuser',
            name='followers',
            field=models.ManyToManyField(blank=True, related_name='is_followed_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
