from django.contrib import admin

from .models import Booking, Movie, Seat


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'duration')


@admin.register(Seat)
class SeatAdmin(admin.ModelAdmin):
    list_display = ('seat_number', 'booking_status')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('movie', 'seat', 'user', 'booking_date')
