from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime, timedelta
from .models import *
from django.contrib import messages
from django.urls import path
from . import views
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm, BookingForm
from .models import Booking
from django.views.generic import ListView
from django.views import generic

# login / logout / user registration system
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.success(request, "There was an error logging in, please try again")
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout_user(request):
    logout(request)
    messages.success(request, "You were logged out")
    return redirect('login')


def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Resigstration successful!"))
            return redirect('booking')
    else:
        form = RegisterUserForm()
    return render(request, 'register_user.html', {'form': form, })


# urls to website pages
def index(request):
    return render(request, "index.html", {})


def about(request):
    return render(request, "about.html", {})


def contact(request):
    return render(request, "contact.html", {})


def feedback(request):
    return render(request, "feedback.html", {})


def menu(request):
    return render(request, "menu.html", {})


def notRegistered(request):
    return render(request, "notRegistered.html", {})


# form inputs
def First_name(request):
    if request.method == "POST":
        First_name = request.POST["First_name"]


def Last_name(request):
    if request.method == "POST":
        Last_name = request.POST["Last_name"]


def Email(request):
    if request.method == "POST":
        Email = request.POST["Email"]


def Phone(request):
    if request.method == "POST":
        Phone = request.POST["Phone"]


def account(request):
    bookings = Booking.objects.filter(user=request.user)
    context = {
        'bookings': bookings
    }
    return render(request, 'account.html', context)


def bookingEdit(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('account')
    form = BookingForm(instance=booking)
    context = {
        'form': form
    }
    return render(request, 'bookingEdit.html', context)


def bookingDelete(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    booking.delete()
    return redirect('account')


def booking(request):
    if request.method == 'POST':

        day = request.POST.get('day')
        guests = request.POST.get('guests')
        First_name = request.POST.get('First_name')
        Last_name = request.POST.get('Last_name')
        Email = request.POST.get('Email')
        Phone = request.POST.get('Phone')

        # Store day and service in django session:
        request.session['day'] = day
        request.session['guests'] = guests
        request.session['First_name'] = First_name
        request.session['Last_name'] = Last_name
        request.session['Email'] = Email
        request.session['Phone'] = Phone

        today = datetime.now()
        minDate = today.strftime('%Y-%m-%d')
        deltatime = today + timedelta(days=21)
        strdeltatime = deltatime.strftime('%Y-%m-%d')
        maxDate = strdeltatime
        time = request.POST.get("time")
        date = dayToWeekday(day)

        if Booking.objects.filter(day=day).count() < 11:
            if Booking.objects.filter(day=day, time=time).count() < 1:
                BookingForm = Booking.objects.get_or_create(
                    guests=guests,
                    First_name=First_name,
                    Last_name=Last_name,
                    Email=Email,
                    Phone=Phone,
                    day=day,
                    time=time,
                    user=request.user,
                )
                messages.success(request, "Booking Saved!")
                return redirect('account')
            else:
                messages.success(request, "The Selected Time Has Been Reserved Before!")
        else:
            messages.success(request, "The Selected Day Is Full!")
    # Calling 'validWeekday' Function to Loop days you want in the next 21 days:
    weekdays = validWeekday(22)

    # Only show the days that are not full:
    validateWeekdays = isWeekdayValid(weekdays)
    return render(request, 'booking.html', {
        'times': ["9 AM", "10 AM", "11 AM", "12 PM", "3 PM", "4 PM", "5 PM", "6 PM", "7 PM", "8 PM", "9 PM"],
        'weekdays': validWeekday(22),
        'validateWeekdays': isWeekdayValid(weekdays),
    })


def dayToWeekday(x):
    z = datetime.strptime(x, "%Y-%m-%d")
    y = z.strftime('%A')
    return y


def validWeekday(days):
    # Loop days you want in the next 21 days:
    today = datetime.now()
    weekdays = []
    for i in range (0, days):
        x = today + timedelta(days=i)
        y = x.strftime('%A')
        if y == 'Tuesday' or y == 'Wednesday' or y == 'Thursday' or y == 'Friday' or y == 'Saturday' or y == 'Sunday':
            weekdays.append(x.strftime('%Y-%m-%d'))
    return weekdays


def isWeekdayValid(x):
    validateWeekdays = []
    for j in x:
        if Booking.objects.filter(day=j).count() < 10:
            validateWeekdays.append(j)
    return validateWeekdays


def checkTime(times, day):
    # Only show the time of the day that has not been selected before:
    x = []
    for k in times:
        if Booking.objects.filter(day=day, time=k).count() < 1:
            x.append(k)
    return x


def checkEditTime(times, day, id):
    # Only show the time of the day that has not been selected before:
    x = []
    booking = Booking.objects.get(pk=id)
    time = booking.time
    for k in times:
        if Booking.objects.filter(day=day, time=k).count() < 1 or time == k:
            x.append(k)
    return x
