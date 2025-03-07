from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('hotel/<int:hotel_id>/', views.room_list, name='room_list'),
    path('book/<int:room_id>/', views.book_room, name='book_room'),
    path('booking/<int:booking_id>/', views.booking_confirmation, name='booking_confirmation'),
    path('cancel/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
]