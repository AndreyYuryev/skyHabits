# Generated by Django 5.0.3 on 2024-03-29 13:38

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0010_habit_started_on_habit_started_time_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='habit',
            name='started_time',
        ),
        migrations.AlterField(
            model_name='habit',
            name='started_on',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='начало действия'),
        ),
    ]
