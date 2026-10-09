from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.test import APITestCase

from .models import Booking, Movie, Seat


class BookingModelsTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='alice',
            email='alice@example.com',
            password='testpass123',
        )
        self.movie = Movie.objects.create(
            title='Inception',
            description='A mind-bending thriller.',
            release_date='2010-07-16',
            duration=148,
        )
        self.seat = Seat.objects.create(seat_number='A1', booking_status=False)

    def test_movie_is_created_with_expected_fields(self):
        self.assertEqual(self.movie.title, 'Inception')
        self.assertEqual(self.movie.duration, 148)

    def test_booking_links_movie_seat_and_user(self):
        booking = Booking.objects.create(
            movie=self.movie,
            seat=self.seat,
            user=self.user,
        )
        self.assertEqual(booking.movie, self.movie)
        self.assertEqual(booking.seat, self.seat)
        self.assertEqual(booking.user, self.user)


class BookingApiTests(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='bob',
            email='bob@example.com',
            password='testpass123',
        )
        self.movie = Movie.objects.create(
            title='Arrival',
            description='A language of time and emotion.',
            release_date='2016-11-11',
            duration=116,
        )
        self.seat = Seat.objects.create(seat_number='B2', booking_status=False)
        Booking.objects.create(movie=self.movie, seat=self.seat, user=self.user)

    def test_movie_list_api_returns_movies(self):
        response = self.client.get('/api/movies/')
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.data), 1)

    def test_booking_list_api_returns_bookings(self):
        response = self.client.get('/api/bookings/')
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.data), 1)
