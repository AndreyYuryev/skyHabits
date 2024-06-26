# Generated by Django 5.0.3 on 2024-03-29 12:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0007_rename_habits_habit'),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='место')),
                ('description', models.CharField(blank=True, max_length=255, null=True, verbose_name='описание места')),
            ],
            options={
                'verbose_name': 'Место',
                'verbose_name_plural': 'Место',
            },
        ),
        migrations.AlterField(
            model_name='habit',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='habits.place', verbose_name='место применения'),
        ),
    ]
