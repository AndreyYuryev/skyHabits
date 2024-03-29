from django.db import models
from django.conf import settings
from habits.utils import NULLABLE
from django.utils import timezone


class Place(models.Model):
    name = models.CharField(max_length=100, verbose_name='место')
    description = models.CharField(max_length=255, verbose_name='описание места', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Место'


class Interval(models.Model):
    name = models.CharField(max_length=100, verbose_name='название интервала')
    days = models.IntegerField(default=0, verbose_name='интервал в днях')
    hours = models.IntegerField(default=0, verbose_name='интервал в часах')
    minutes = models.IntegerField(verbose_name='интервал в минутах')

    def __str__(self):
        return f'{self.name} - {self.days} дней {self.hours} часов {self.minutes} минут'

    class Meta:
        verbose_name = 'Интервал'
        verbose_name_plural = 'Интервалы'


class Habit(models.Model):
    action = models.CharField(max_length=100, verbose_name='действие')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='пользователь')
    place = models.ForeignKey(Place, on_delete=models.CASCADE, verbose_name='место применения', **NULLABLE)
    interval = models.ForeignKey(Interval, on_delete=models.CASCADE, verbose_name='периодичность', **NULLABLE)
    started_on = models.DateTimeField(default=timezone.now, verbose_name='начало действия')
    is_pleasant = models.BooleanField(default=False, verbose_name='приятная привычка')
    linked_habit = models.ForeignKey('Habit', on_delete=models.SET_NULL,
                                     verbose_name='связанная привычка', **NULLABLE)
    reward = models.CharField(max_length=100, verbose_name='вознаграждение', **NULLABLE)
    is_public = models.BooleanField(default=False, verbose_name='публичная')
    execution_time = models.IntegerField(default=120, verbose_name='время на выполнение в секундах')

    def __str__(self):
        return f'{self.action}'

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
        ordering = ['id']
