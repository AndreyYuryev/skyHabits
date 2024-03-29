from rest_framework.serializers import ValidationError
from habits.models import Habit


class ExecutionTimeValidator:
    """ Время выполнения должно быть не больше 120 секунд. """

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        field_value = dict(value).get(self.field)
        if int(field_value) >= 120:
            raise ValidationError('Время выполнения не более 120 секунд')


class IntervalValidator:
    """ Нельзя выполнять привычку реже, чем 1 раз в 7 дней. """

    def __init__(self):
        self.field_days = 'days'
        self.field_hours = 'hours'
        self.field_minutes = 'minutes'

    def __call__(self, value):
        field_days = dict(value).get(self.field_days)
        field_hours = dict(value).get(self.field_hours)
        field_minutes = dict(value).get(self.field_minutes)
        if int(field_days) > 7 or int(field_days) == 7 and (int(field_hours) > 0 or int(field_minutes) > 0):
            raise ValidationError('Нельзя выполнять привычку реже, чем 1 раз в 7 дней')


class HabitAndRewardValidator:
    """ Исключить одновременный выбор связанной привычки и указания вознаграждения """

    def __init__(self, habit, reward):
        self.field_habit = habit
        self.field_reward = reward

    def __call__(self, value):
        habit = dict(value).get(self.field_habit)
        reward = dict(value).get(self.field_reward)
        if habit is not None and reward != '':
            raise ValidationError('Исключить одновременный выбор связанной привычки и указания вознаграждения')


class PleasantHabitValidator:
    """ У приятной привычки не может быть вознаграждения или связанной привычки """

    def __init__(self, pleasant, reward, linked_habit):
        self.field_pleasant = pleasant
        self.field_reward = reward
        self.field_linked_habit = linked_habit

    def __call__(self, value):
        pleasant = dict(value).get(self.field_pleasant)
        reward = dict(value).get(self.field_reward)
        linked_habit = dict(value).get(self.field_linked_habit)
        if pleasant and (reward != '' or linked_habit is not None):
            raise ValidationError('У приятной привычки не может быть вознаграждения или связанной привычки')


class LinkedHabitValidator:
    """ В связанные привычки могут попадать только привычки с признаком приятной привычки """

    def __init__(self, linked_habit):
        self.field_linked_habit = linked_habit

    def __call__(self, value):
        linked_habit = value.get(self.field_linked_habit)
        if linked_habit is not None:
            habit = Habit.objects.filter(pk=linked_habit.id).first()
            if habit is not None and not habit.is_pleasant:
                raise ValidationError(
                    'В связанные привычки могут попадать только привычки с признаком приятной привычки')
