from rest_framework.serializers import ValidationError


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
