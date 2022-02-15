# Generated by Django 3.2.8 on 2021-11-24 12:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_availability_education_language'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('company_name', models.CharField(max_length=255)),
                ('company_email', models.EmailField(max_length=254, null=True)),
                ('company_website', models.URLField(null=True)),
                ('position', models.CharField(max_length=255)),
                ('business_scale', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='other_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='phone',
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='end_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='start_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.CreateModel(
            name='JobsPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('qualification', models.CharField(max_length=255)),
                ('requirement', models.CharField(max_length=255)),
                ('benefit', models.CharField(max_length=255, null=True)),
                ('categories', models.TextField()),
                ('job_type', models.CharField(max_length=255)),
                ('tags', models.CharField(max_length=255)),
                ('validity', models.BooleanField(default=True)),
                ('availability', models.CharField(choices=[['available', 'available'], ['hide', 'hide'], ['delete', 'deleted']], default='available', max_length=255)),
                ('expiry', models.DateField(null=True)),
                ('applications', models.PositiveIntegerField(default=0)),
                ('access', models.CharField(choices=[['public', 'public'], ['private', 'private'], ['verified', 'verified']], default='public', max_length=255)),
                ('budget_start', models.CharField(max_length=255)),
                ('budget_end', models.CharField(max_length=255)),
                ('is_remote', models.BooleanField(default=False)),
                ('location', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('employer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='job_employer', to='api.employer')),
            ],
        ),
        migrations.AddField(
            model_name='employer',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('other_name', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=6)),
                ('phone', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255, null=True)),
                ('about', models.TextField(null=True)),
                ('display_picture', models.URLField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ApplyJob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[['processing', 'processing'], ['accept', 'accepted'], ['shortlist', 'shortlisted'], ['decline', 'declined']], default='processing', max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('applicant', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='job_applicant', to='api.employee')),
                ('job', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='job', to='api.jobspost')),
            ],
        ),
        migrations.AlterField(
            model_name='availability',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='availability', to='api.employee'),
        ),
        migrations.AlterField(
            model_name='education',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='education', to='api.employee'),
        ),
        migrations.AlterField(
            model_name='language',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='language', to='api.employee'),
        ),
        migrations.AlterField(
            model_name='skills',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skill', to='api.employee'),
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='work_experience', to='api.employee'),
        ),
    ]
