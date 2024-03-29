from django.shortcuts import render
from rest_framework import viewsets, generics
from habits.serializers import HabitSerializer, PlaceSerializer, IntervalSerializer
from habits.models import Habit, Place, Interval
from habits.pagination import HabitPaginator


class PlaceViewSet(viewsets.ModelViewSet):
    serializer_class = PlaceSerializer
    queryset = Place.objects.all()


class IntervalViewSet(viewsets.ModelViewSet):
    serializer_class = IntervalSerializer
    queryset = Interval.objects.all()


class HabitViewSet(viewsets.ModelViewSet):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    pagination_class = HabitPaginator
