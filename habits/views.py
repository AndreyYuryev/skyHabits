from django.shortcuts import render
from rest_framework import viewsets, generics
from habits.serializators import HabitSerializer
from habits.models import Habit


# Create your views here.
class HabitsViewSet(viewsets.ModelViewSet):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()