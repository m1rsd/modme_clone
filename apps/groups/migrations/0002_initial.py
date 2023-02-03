# Generated by Django 4.1.5 on 2023-02-03 10:29

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('groups', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='coursegroup',
            name='students',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='coursegroup',
            name='teachers',
            field=models.ManyToManyField(related_name='teachers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='course',
            name='branch',
            field=models.ManyToManyField(to='groups.branch'),
        ),
    ]
