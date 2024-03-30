from celery import shared_task
from habits.services import MyBot
from habits.models import Habit, Interval, Place
from datetime import timedelta, datetime
import pytz


@shared_task
def notify():
    MSK = pytz.timezone('Europe/Moscow')
    my_bot = MyBot()
    messages = ['Внимание!', ]
    habits = Habit.objects.all()
    time_from = datetime.now().astimezone()
    time_till = time_from + timedelta(hours=1)
    for habit in habits:
        place = Place.objects.filter(pk=habit.place.id).first()
        interval = Interval.objects.filter(pk=habit.interval.id).first()
        delta = timedelta(days=interval.days, hours=interval.hours, minutes=interval.minutes)
        started_time = habit.started_on
        current_time = started_time
        if current_time >= time_from:
            if delta:
                while time_till >= current_time:
                    message = (f'Напоминание: я буду {habit.action} в {current_time.astimezone(MSK).isoformat()} в '
                               f'{place.name}. На выполнение {habit.execution_time} секунд.')
                    messages.append(message)
                    current_time += delta
            else:
                # однократно
                if time_from <= current_time <= time_till:
                    message = (f'Напоминание: я буду {habit.action} в {current_time.astimezone(MSK).isoformat()} в '
                               f'{place.name}. На выполнение {habit.execution_time} секунд.')
                    messages.append(message)
    for msg in messages:
        my_bot.send_message(msg)
