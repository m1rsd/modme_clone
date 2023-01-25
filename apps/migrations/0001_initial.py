# Generated by Django 4.1.5 on 2023-01-24 20:47

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, verbose_name='branch_name')),
                ('address', models.CharField(max_length=255, verbose_name='branch_location')),
                ('phone_number', models.IntegerField(unique=True, verbose_name='phone_number_of_branch')),
                ('about', models.TextField()),
                ('image', models.ImageField(upload_to='images/')),
            ],
            options={
                'verbose_name': 'Branch',
                'verbose_name_plural': 'Branch',
                'db_table': 'branches',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, verbose_name='role_name')),
            ],
            options={
                'verbose_name': 'Role',
                'verbose_name_plural': 'Role',
                'db_table': 'roles',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('full_name', models.CharField(max_length=64, verbose_name='full_name')),
                ('phone_number', models.IntegerField(unique=True, verbose_name='phone_number')),
                ('birth', models.DateField(blank=True, null=True, verbose_name='birth_date')),
                ('gender', models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female')], max_length=25, null=True, verbose_name='gender')),
                ('photo', models.ImageField(blank=True, default='media/profile.jpg', null=True, upload_to='profiles/', verbose_name='photo_of_profile')),
                ('branch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='apps.branch')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('role', models.ManyToManyField(to='apps.role')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Manager',
                'verbose_name_plural': 'Managers',
                'db_table': 'users',
            },
        ),
    ]
