# Generated by Django 5.0.3 on 2024-03-30 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0012_rename_user_habit_created_by'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='habit',
            options={'ordering': ['id'], 'verbose_name': 'Привычка', 'verbose_name_plural': 'Привычки'},
        ),
        migrations.AlterField(
            model_name='habit',
            name='is_pleasant',
            field=models.BooleanField(default=False, verbose_name='приятная привычка'),
        ),
        migrations.AlterField(
            model_name='interval',
            name='minutes',
            field=models.IntegerField(default=0, verbose_name='интервал в минутах'),
        ),
    ]
