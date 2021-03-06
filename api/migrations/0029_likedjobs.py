# Generated by Django 3.2.8 on 2022-02-11 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0028_auto_20220201_1804'),
    ]

    operations = [
        migrations.CreateModel(
            name='LikedJobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_like', to='api.jobspost')),
                ('liker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='liker', to='api.employee')),
            ],
        ),
    ]
