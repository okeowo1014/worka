# Generated by Django 3.2.8 on 2021-12-23 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_auto_20211220_0200'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobspost',
            name='message_channel',
            field=models.CharField(default='', max_length=16),
        ),
        migrations.AlterField(
            model_name='employee',
            name='display_picture',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='gender',
            field=models.CharField(choices=[['male', 'male'], ['female', 'female']], max_length=6),
        ),
    ]
