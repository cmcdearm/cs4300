from django.contrib import messages
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework import viewsets

from .models import Booking, Movie, Seat
from .serializers import BookingSerializer, MovieSerializer, SeatSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all().order_by('title')
    serializer_class = MovieSerializer


class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all().order_by('seat_number')
    serializer_class = SeatSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all().order_by('-booking_date')
    serializer_class = BookingSerializer


def ensure_demo_data():
    if Movie.objects.exists():
        return

    movie = Movie.objects.create(
        title='The Nightmare Before Christmas',
        description='Jack Skellington, the Pumpkin King of Halloween Town, discovers Christmas Town and tries to take over Christmas.',
        release_date='1993-10-13',
        duration=76,
    )
    for seat_number in ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']:
        Seat.objects.create(seat_number=seat_number, booking_status=False)

    # Keep the first movie in the app ready to browse immediately.
    return movie


def movie_list_view(request):
    ensure_demo_data()
    movies = Movie.objects.all().order_by('title')
    return render(request, 'bookings/movie_list.html', {'movies': movies})


def book_seat_view(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    seats = Seat.objects.filter(booking_status=False).order_by('seat_number')

    if request.method == 'POST':
        seat_id = request.POST.get('seat_id')
        if not seat_id:
            messages.error(request, 'Please select a seat.')
            return redirect('book_seat', movie_id=movie.id)

        seat = get_object_or_404(Seat, id=seat_id)
        if seat.booking_status:
            messages.error(request, 'That seat is already booked.')
            return redirect('book_seat', movie_id=movie.id)

        if request.user.is_authenticated:
            user = request.user
        else:
            user, _ = get_user_model().objects.get_or_create(
                username='guest',
                defaults={'email': 'guest@example.com'},
            )

        seat.booking_status = True
        seat.save()
        Booking.objects.create(movie=movie, seat=seat, user=user)
        messages.success(request, f'Booking confirmed for {movie.title} seat {seat.seat_number}.')
        return redirect('booking_history')

    return render(request, 'bookings/seat_booking.html', {'movie': movie, 'seats': seats})


def booking_history_view(request):
    if request.user.is_authenticated:
        bookings = Booking.objects.filter(user=request.user).order_by('-booking_date')
    else:
        bookings = Booking.objects.order_by('-booking_date')[:10]

    return render(request, 'bookings/booking_history.html', {'bookings': bookings})
