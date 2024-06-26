# Generated by Django 5.0.3 on 2024-03-28 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=100, verbose_name='место')),
                ('started_on', models.DateField(verbose_name='начало действия')),
                ('time', models.TimeField(verbose_name='время действия')),
                ('action', models.CharField(max_length=100, verbose_name='действие')),
                ('is_public', models.BooleanField(default=False, verbose_name='публичная')),
                ('execution_time', models.IntegerField(default=1, verbose_name='время на выполнение')),
            ],
            options={
                'verbose_name': 'Привычка',
                'verbose_name_plural': 'Привычки',
            },
        ),
    ]
