from celery import shared_task
from django.conf import settings
from habits.services import MyBot
from habits.models import Habit

@shared_task
def inform():
    my_bot = MyBot()
    habits = Habit.objects.all()
    for habit in habits:
        my_bot.send_message(f'привычка {habit.action}')
