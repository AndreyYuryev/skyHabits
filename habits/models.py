from django.db import models
from django.conf import settings
from habits.utils import NULLABLE, REGULARITY_VALUES, DAILY


# Create your models here.
class Habit(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='пользователь')
    place = models.CharField(max_length=100, verbose_name='место')
    # started_on = models.DateField(verbose_name='начало действия')
    # time = models.TimeField(verbose_name='время действия')
    action = models.CharField(max_length=100, verbose_name='действие')
    # pleasant_habit = models.ForeignKey('Habit', on_delete=models.SET_NULL,
    #                                    verbose_name='полезная привычка', **NULLABLE)
    is_pleasant = models.BooleanField(default=False)
    linked_habit = models.ForeignKey('Habit', on_delete=models.SET_NULL,
                                     verbose_name='связанная привычка', **NULLABLE)
    regularity = models.CharField(max_length=1, choices=REGULARITY_VALUES, default=DAILY,
                                  verbose_name='периодичность')
    reward = models.CharField(max_length=100, verbose_name='вознаграждение', **NULLABLE)
    is_public = models.BooleanField(default=False, verbose_name='публичная')
    execution_time = models.IntegerField(default=1, verbose_name='время на выполнение')

    def __str__(self):
        return f'{self.action}'

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
