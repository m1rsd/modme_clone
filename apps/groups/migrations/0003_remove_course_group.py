# Generated by Django 4.1.5 on 2023-01-30 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='group',
        ),
    ]
