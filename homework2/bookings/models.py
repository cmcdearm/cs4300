from django.conf import settings
from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_date = models.DateField()
    duration = models.IntegerField(help_text='Duration in minutes')

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Seat(models.Model):
    seat_number = models.CharField(max_length=10, unique=True)
    booking_status = models.BooleanField(default=False)

    class Meta:
        ordering = ['seat_number']

    def __str__(self):
        return self.seat_number


class Booking(models.Model):
    movie = models.ForeignKey(Movie, related_name='bookings', on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, related_name='bookings', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='bookings', on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-booking_date']

    def __str__(self):
        return f'{self.user.username} booked {self.movie.title} for seat {self.seat.seat_number}'
