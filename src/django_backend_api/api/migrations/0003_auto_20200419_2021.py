# Generated by Django 2.2.12 on 2020-04-19 20:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200418_2235'),
    ]

    operations = [
        migrations.RenameField(
            model_name='portfolio',
            old_name='skill',
            new_name='skills',
        ),
        migrations.RenameField(
            model_name='skill',
            old_name='language',
            new_name='skill',
        ),
        migrations.RemoveField(
            model_name='portfolio',
            name='college',
        ),
        migrations.AddField(
            model_name='college',
            name='degree',
            field=models.CharField(default='', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='college',
            name='from_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='college',
            name='grade',
            field=models.CharField(default='0.0 GPA', max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='college',
            name='to_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='education',
            field=models.ManyToManyField(to='api.College'),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.CharField(default='', max_length=100)),
                ('about', models.CharField(default='', max_length=400, null=True)),
                ('feature', models.CharField(default='', max_length=200)),
                ('tech_stack', models.CharField(default='', max_length=100)),
                ('project_url', models.URLField(max_length=400, null=True)),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interest', models.CharField(default='', max_length=100)),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(default='', max_length=50)),
                ('address', models.CharField(default='', max_length=200)),
                ('about', models.CharField(default='', max_length=500, null=True)),
                ('company_url', models.URLField(max_length=400, null=True)),
                ('joining_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('to_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('currently_working', models.BooleanField(default=False)),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Certification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificate', models.CharField(default='', max_length=100)),
                ('about', models.CharField(default='', max_length=100)),
                ('certificate_url', models.URLField(max_length=400)),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('achievement', models.CharField(default='', max_length=100)),
                ('when', models.DateTimeField(auto_now_add=True, null=True)),
                ('where', models.DateTimeField(auto_now_add=True, null=True)),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('highlights', models.CharField(default='', max_length=100)),
                ('about', models.CharField(default='', max_length=900)),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='portfolio',
            name='about',
            field=models.ManyToManyField(to='api.About'),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='achievement',
            field=models.ManyToManyField(to='api.Achievement'),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='interest',
            field=models.ManyToManyField(to='api.Interest'),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='work_experience',
            field=models.ManyToManyField(to='api.Company'),
        ),
    ]