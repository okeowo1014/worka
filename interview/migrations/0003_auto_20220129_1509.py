# Generated by Django 3.2.8 on 2022-01-29 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interview', '0002_auto_20220129_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objectiveinterviewquestions',
            name='sub_answer',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='theoryinterviewquestions',
            name='sub_answer',
            field=models.TextField(default=''),
        ),
    ]
