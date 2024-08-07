# Generated by Django 5.0.7 on 2024-07-17 12:13

import django.contrib.auth.models
import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('base', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('organisation', models.CharField(blank=True, max_length=50, null=True)),
                ('work_email', models.EmailField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='JobOpenings',
            fields=[
                ('role', models.CharField(max_length=50)),
                ('job_Id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('description', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('organisation_Id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('location', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='JobReferrals',
            fields=[
                ('referral_Id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('job_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_referrals', to='base.jobopenings')),
                ('user_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_referrals', to='base.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.room')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddConstraint(
            model_name='organisation',
            constraint=models.UniqueConstraint(fields=('name',), name='unique_organisation_name'),
        ),
        migrations.AddField(
            model_name='jobopenings',
            name='organisation_Id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_openings', to='base.organisation'),
        ),
    ]
