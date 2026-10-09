from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'movies', views.MovieViewSet)
router.register(r'seats', views.SeatViewSet)
router.register(r'bookings', views.BookingViewSet)

urlpatterns = [
    path('', views.movie_list_view, name='movie_list'),
    path('book/<int:movie_id>/', views.book_seat_view, name='book_seat'),
    path('history/', views.booking_history_view, name='booking_history'),
    path('api/', include(router.urls)),
]
