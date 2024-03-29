from rest_framework import serializers
from habits.models import Habit


class HabitSerializer(serializers.ModelSerializer):
    # subscribed = serializers.HiddenField(default=True)

    class Meta:
        model = Habit
        fields = '__all__'
