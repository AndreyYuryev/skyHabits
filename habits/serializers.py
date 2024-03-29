from rest_framework import serializers
from habits.models import Habit, Place, Interval
from habits.validation import ExecutionTimeValidator, IntervalValidator, HabitAndRewardValidator


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'


class IntervalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interval
        fields = '__all__'
        validators = [IntervalValidator(), ]


class HabitSerializer(serializers.ModelSerializer):
    # subscribed = serializers.HiddenField(default=True)

    class Meta:
        model = Habit
        fields = '__all__'
        validators = [ExecutionTimeValidator(field='execution_time'),
                      HabitAndRewardValidator(habit='linked_habit', reward='reward'), ]
