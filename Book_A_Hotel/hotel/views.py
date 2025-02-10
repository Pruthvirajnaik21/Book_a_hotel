from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Hotel, Room, Booking
from .forms import BookingForm

def home(request):
    hotels = Hotel.objects.all()
    return render(request, 'hotel/home.html', {'hotels': hotels})

def room_list(request, hotel_id):
    hotel = get_object_or_404(Hotel, id=hotel_id)
    rooms = Room.objects.filter(hotel=hotel, is_available=True)
    return render(request, 'hotel/room_list.html', {'hotel': hotel, 'rooms': rooms})

def book_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    if not room.is_available:
        messages.error(request, 'This room is already booked!')
        return redirect('room_list', hotel_id=room.hotel.id)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.room = room
            booking.hotel = room.hotel
            booking.save()
            room.is_available = False
            room.save()
            messages.success(request, 'Room booked successfully!')
            return redirect('booking_confirmation', booking.id)
    else:
        form = BookingForm()
    return render(request, 'hotel/book_room.html', {'form': form, 'room': room})

def booking_confirmation(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    return render(request, 'hotel/booking_confirmation.html', {'booking': booking})

def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    room = booking.room
    room.is_available = True
    room.save()
    booking.delete()
    messages.success(request, 'Booking canceled successfully!')
    return redirect('home')