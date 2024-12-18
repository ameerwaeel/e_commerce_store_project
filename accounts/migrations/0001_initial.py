# Generated by Django 5.1.3 on 2024-11-30 19:42

import datetime
import django.db.models.deletion
import django_countries.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, null=True)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('join_date', models.DateTimeField(default=datetime.datetime.now)),
                ('address', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='user_image/')),
                ('uesr', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
            },
        ),
    ]
