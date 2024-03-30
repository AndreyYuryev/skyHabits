from django.test import TestCase
from rest_framework.test import APITestCase
from users.models import User
from rest_framework import status
from habits.models import Place, Interval, Habit
import json


class UserAPITestCase(APITestCase):

    def setUp(self):
        self.user1 = User.objects.create(email='test1@sky.pro', password='123qaz')
        self.usera = User.objects.create(email='testA@sky.pro', password='123qaz')

    def test_get(self):
        print('get')
        url = '/api/v1/users/'
        self.client.force_authenticate(user=self.user1)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post(self):
        print('post')
        self.post_data = {"email": 'testx@sky.pro', "password": '123qaz', "first_name": 'testx',
                          "last_name": 'skypro', }
        url = '/api/v1/users/'
        self.client.force_authenticate(user=self.user1)
        response = self.client.post(url, data=json.dumps(self.post_data, indent=4), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update(self):
        print('update')
        self.update_data = {"email": 'test1@sky.pro', "password": '123qaz', "first_name": 'testA1',
                            "last_name": 'skypro', }
        id = User.objects.filter(email='test1@sky.pro').first().id
        url = f'/api/v1/users/{id}/'
        self.client.force_authenticate(user=self.user1)
        response = self.client.put(url, self.update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete(self):
        print('delete')
        id = User.objects.filter(email='test1@sky.pro').first().id
        url = f'/api/v1/users/{id}/'
        self.client.force_authenticate(user=self.user1)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class PlaceAPITestCase(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create(email='test1@sky.pro', password='123qaz')
        #         self.user2 = User.objects.create(email='test2@sky.pro', password='123qaz')
        self.place1 = Place.objects.create(name='Улица', description='Улица')

    #         # self.place2 = Place.objects.create(name='Работа', description='Место работы')
    def test_get(self):
        print('get')
        url = '/api/v1/place/'
        self.client.force_authenticate(user=self.user1)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post(self):
        print('post')
        self.post_data = {"name": "Работа", "description": "Место на работе"}
        url = '/api/v1/place/'
        self.client.force_authenticate(user=self.user1)
        response = self.client.post(url, data=json.dumps(self.post_data, indent=4), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update(self):
        print('update')
        self.update_data = {"name": "Улица", "description": "Место на улице исправлено"}
        id = Place.objects.filter(name='Улица').first().id
        url = f'/api/v1/place/{id}/'
        self.client.force_authenticate(user=self.user1)
        response = self.client.put(url, self.update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete(self):
        print('delete')
        id = Place.objects.filter(name='Улица').first().id
        url = f'/api/v1/place/{id}/'
        self.client.force_authenticate(user=self.user1)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class IntervalAPITestCase(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create(email='test1@sky.pro', password='123qaz')
        #         self.user2 = User.objects.create(email='test2@sky.pro', password='123qaz')
        self.interval1 = Interval.objects.create(name='Один час', days=0, hours=1, minutes=0)

    #         # self.place2 = Place.objects.create(name='Работа', description='Место работы')
    def test_get(self):
        print('get')
        url = '/api/v1/interval/'
        self.client.force_authenticate(user=self.user1)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post(self):
        print('post')
        self.post_data = {"name": "Четверть часа",
                          "days": 0,
                          "hours": 0,
                          "minutes": 15}
        url = '/api/v1/interval/'
        self.client.force_authenticate(user=self.user1)
        response = self.client.post(url, data=json.dumps(self.post_data, indent=4), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update(self):
        print('update')
        self.update_data = {"name": "Три четверти часа",
                            "days": 0,
                            "hours": 0,
                            "minutes": 45}
        id = Interval.objects.filter(name='Один час').first().id
        url = f'/api/v1/interval/{id}/'
        self.client.force_authenticate(user=self.user1)
        response = self.client.put(url, self.update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete(self):
        print('delete')
        id = Interval.objects.filter(name='Один час').first().id
        url = f'/api/v1/interval/{id}/'
        self.client.force_authenticate(user=self.user1)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class HabitAPITestCase(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create(email='test1@sky.pro', password='123qaz')
        self.user2 = User.objects.create(email='test2@sky.pro', password='123qaz')
        self.place = Place.objects.create(name='Работа', description='Место работы')
        self.interval = Interval.objects.create(name='Один час', days=0, hours=1, minutes=0)
        self.habit1 = Habit.objects.create(action='Выпить стакан воды', is_pleasant=False,
                                           execution_time=60, place=self.place, interval=self.interval,
                                           created_by=self.user1)
        self.habit2 = Habit.objects.create(action='Прочитать почту', is_pleasant=False,
                                           execution_time=60, place=self.place, interval=self.interval,
                                           created_by=self.user1, is_public=True)

    def test_get(self):
        print('get')
        url = '/api/v1/habit/'
        self.client.force_authenticate(user=self.user1)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post(self):
        print('post')
        self.post_data = {"action": "Отжаться от пола 20 раз",
                          "is_pleasant": True,
                          "reward": "",
                          "is_public": False,
                          "execution_time": 60,
                          "place": self.place.pk,
                          "interval": self.interval.pk, }
        url = '/api/v1/habit/'
        self.client.force_authenticate(user=self.user1)
        response = self.client.post(url, data=json.dumps(self.post_data, indent=4), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_update(self):
        print('update')
        # place = Place.objects.filter(name=self.place.name).first()
        # interval = Interval.objects.filter(name=self.interval.name).first()
        # user = User.objects.filter(email=self.user1.email).first()
        # self.update_data = {"action": 'Прочитать почту', "is_pleasant": False,
        #                     "execution_time": 60, "place": place, "interval": interval,
        #                     "created_by": user, "is_public": False}
        self.update_data = {"action": "Прочитать почту", "is_public": False, "execution_time": 90}
        id = Habit.objects.filter(action='Прочитать почту').first().id
        url = f'/api/v1/habit/{id}/'
        self.client.force_authenticate(user=self.user1)
        response = self.client.put(url, self.update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete(self):
        print('delete')
        id = Habit.objects.filter(action='Выпить стакан воды').first().id
        url = f'/api/v1/habit/{id}/'
        self.client.force_authenticate(user=self.user1)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_public_habits_get(self):
        print('get')
        url = '/api/v1/public/'
        self.client.force_authenticate(user=self.user2)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_own_habits_get(self):
        print('get')
        id = Habit.objects.filter(action='Выпить стакан воды').first().id
        url = f'/api/v1/habit/{id}/'
        self.client.force_authenticate(user=self.user1)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_foreign_habits_get(self):
        print('get')
        id = Habit.objects.filter(action='Выпить стакан воды').first().id
        url = f'/api/v1/habit/{id}/'
        self.client.force_authenticate(user=self.user2)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
