# Generated by Django 3.2.8 on 2021-12-11 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_auto_20211207_1452'),
        ('notifier', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='directemployeenotifier',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.employee'),
        ),
        migrations.AlterField(
            model_name='directemployernotifier',
            name='employer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.employer'),
        ),
    ]
