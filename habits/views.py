from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from habits.serializers import HabitSerializer, PlaceSerializer, IntervalSerializer
from habits.models import Habit, Place, Interval
from habits.pagination import HabitPaginator
from habits.permissions import IsOwner


class PlaceViewSet(viewsets.ModelViewSet):
    serializer_class = PlaceSerializer
    queryset = Place.objects.all()
    permission_classes = [IsAuthenticated, ]


class IntervalViewSet(viewsets.ModelViewSet):
    serializer_class = IntervalSerializer
    queryset = Interval.objects.all()
    permission_classes = [IsAuthenticated, ]


class HabitViewSet(viewsets.ModelViewSet):
    serializer_class = HabitSerializer
    pagination_class = HabitPaginator

    def get_queryset(self):
        if self.action == 'list':
            return Habit.objects.filter(created_by=self.request.user)
        else:
            return Habit.objects.all()

    def get_permissions(self):
        if (self.action == 'list' or self.action == 'retrieve'
                or self.action == 'update' or self.action == 'partial_update'):
            permission_classes = [IsAuthenticated, IsOwner]
        elif self.action == 'create':
            permission_classes = [IsAuthenticated, ]
        else:
            permission_classes = [IsAuthenticated, IsOwner]
        return [permission() for permission in permission_classes]


class PublicHabitListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        return Habit.objects.filter(is_public=True)
