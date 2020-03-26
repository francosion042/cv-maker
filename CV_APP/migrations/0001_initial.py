# Generated by Django 3.0.4 on 2020-03-26 21:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Work_experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.CharField(default='Now', max_length=150, null=True)),
                ('end', models.CharField(default='Now', max_length=150, null=True)),
                ('company', models.CharField(max_length=100)),
                ('role', models.CharField(blank=True, max_length=100)),
                ('description', models.TextField(blank=True)),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('address', models.TextField()),
                ('mobile', models.CharField(max_length=20)),
                ('image', models.ImageField(blank=True, upload_to='media')),
                ('img_name', models.CharField(blank=True, max_length=1000)),
                ('nationality', models.CharField(blank=True, max_length=100)),
                ('state', models.CharField(blank=True, max_length=100)),
                ('skills', models.TextField()),
                ('hobbies', models.TextField(blank=True)),
                ('references', models.TextField(blank=True)),
                ('userid', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.CharField(default='Now', max_length=150, null=True)),
                ('end', models.CharField(default='Now', max_length=150, null=True)),
                ('school', models.CharField(max_length=100)),
                ('descipline', models.CharField(max_length=100)),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
