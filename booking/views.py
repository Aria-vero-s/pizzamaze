from django.shortcuts import render, redirect
from datetime import datetime, timedelta
from .models import *
from django.contrib import messages
from django.urls import path
from . import views


def index(request):
    return render(request, "index.html", {})


def about(request):
    return render(request, "about.html", {})


def contact(request):
    return render(request, "contact.html", {})


def menu(request):
    return render(request, "menu.html", {})


def register(request):
    return render(request, "register.html", {})


# def get_author(user):
#     if user.is_anonymous:
#         guest_user = User.objects.get(username="guest") # or whatever ID or name you use for the placeholder user that no one will be assigned
#         qs = Author.objects.filter(user=guest_user)
#         if qs.exists():
#             return qs[0]
#         return None
#     else:
#         qs = Author.objects.filter(user=user)
#         if qs.exists():
#             return qs[0]
#         return None

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

def new_record(request):
    form = OrderForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        author = get_author(request.user)
        form.instance.login_user = author
        form.save()
        return redirect(all_records)

    context = {
        'form': form
    }
    return render(request, 'orders/form.html', context)

def booking(request):
    # Calling 'validWeekday' Function to Loop days you want in the next 21 days:
    weekdays = validWeekday(22)

    # Only show the days that are not full:
    validateWeekdays = isWeekdayValid(weekdays)
    
    if request.method == 'POST':
        guests = request.POST.get('guests')
        day = request.POST.get('day')
        First_name = request.POST.get('First_name')
        Last_name = request.POST.get('Last_name')
        Email = request.POST.get('Email')
        Phone = request.POST.get('Phone')
        if guests == None:
            messages.success(request, "Please Select Guests!")
            return redirect('booking')

        # Store day and service in django session:
        request.session['day'] = day
        request.session['guests'] = guests
        request.session['First_name'] = First_name
        request.session['Last_name'] = Last_name
        request.session['Email'] = Email
        request.session['Phone'] = Phone

        return redirect('bookingSubmit')

    return render(request, 'booking.html', {
            'weekdays': weekdays,
            'validateWeekdays': validateWeekdays,
        })


def bookingSubmit(request):
    user = request.user
    times = [
        "9 AM", "10 AM", "11 AM", "12 PM", "3 PM", "4 PM", "5 PM", "6 PM", "7 PM", "8 PM", "9 PM"
    ]
    today = datetime.now()
    minDate = today.strftime('%Y-%m-%d')
    deltatime = today + timedelta(days=21)
    strdeltatime = deltatime.strftime('%Y-%m-%d')
    maxDate = strdeltatime

    # Get stored data from django session:
    day = request.session.get('day')
    guests = request.session.get('guests')
    First_name = request.session.get('First_name')
    Last_name = request.session.get('Last_name')
    Email = request.session.get('Email')
    Phone = request.session.get('Phone')
    
    # Only show the time of the day that has not been selected before:
    hour = checkTime(times, day)
    if request.method == 'POST':
        time = request.POST.get("time")
        date = dayToWeekday(day)

        if guests != None:
            if day <= maxDate and day >= minDate:
                if date == 'Monday' or date == 'Saturday' or date == 'Wednesday':
                    if Appointment.objects.filter(day=day).count() < 11:
                        if Appointment.objects.filter(day=day, time=time).count() < 1:
                            AppointmentForm = Appointment.objects.get_or_create(
                                user=user,
                                guests=guests,
                                First_name=First_name,
                                Last_name=Last_name,
                                Email=Email,
                                Phone=Phone,
                                day=day,
                                time=time,
                            )
                            messages.success(request, "Booking Saved!")
                            return redirect('index')
                        else:
                            messages.success(request, "The Selected Time Has Been Reserved Before!")
                    else:
                        messages.success(request, "The Selected Day Is Full!")
                else:
                    messages.success(request, "The Selected Date Is Incorrect")
            else:
                messages.success(request, "The Selected Date Isn't In The Correct Time Period!")
        else:
            messages.success(request, "Please select the amounts of guests!")
    return render(request, 'bookingSubmit.html', {
        'times': hour,
    })


def userPanel(request):
    user = request.user
    appointments = Appointment.objects.filter(user=user).order_by('day', 'time', 'First_name', 'Last_name', 'Email', 'Phone')
    return render(request, 'userPanel.html', {
        'user': user,
        'First_name' : First_name,
        'Last_name' : Last_name,
        'Email' : Email,
        'Phone' : Phone,
        'appointments': appointments,
    })


def userUpdate(request, id):
    appointment = Appointment.objects.get(pk=id)
    userdatepicked = appointment.day
    # Copy  booking:
    today = datetime.today()
    minDate = today.strftime('%Y-%m-%d')

    # 24h if statement in template:
    delta24 = (userdatepicked).strftime('%Y-%m-%d') >= (today + timedelta(days=1)).strftime('%Y-%m-%d')
    # Calling 'validWeekday' Function to Loop days you want in the next 21 days:
    weekdays = validWeekday(22)

    # Only show the days that are not full:
    validateWeekdays = isWeekdayValid(weekdays)
    

    if request.method == 'POST':
        guests = request.POST.get('guests')
        day = request.POST.get('day')
        First_name = request.POST.get('First_name')
        Last_name = request.POST.get('Last_name')
        Email = request.POST.get('Email')
        Phone = request.POST.get('Phone')

        #Store day and service in django session:
        request.session['day'] = day
        request.session['guests'] = guests
        request.session['First_name'] = First_name
        request.session['Last_name'] = Last_name
        request.session['Email'] = Email
        request.session['Phone'] = Phone

        return redirect('userUpdateSubmit', id=id)


    return render(request, 'userUpdate.html', {
            'weekdays':weekdays,
            'validateWeekdays':validateWeekdays,
            'delta24': delta24,
            'id': id,
        })

def userUpdateSubmit(request, id):
    user = request.user
    times = [
        "9 AM", "10 AM", "11 AM", "12 PM", "3 PM", "4 PM", "5 PM", "6 PM", "7 PM", "8 PM", "9 PM"
    ]
    today = datetime.now()
    minDate = today.strftime('%Y-%m-%d')
    deltatime = today + timedelta(days=21)
    strdeltatime = deltatime.strftime('%Y-%m-%d')
    maxDate = strdeltatime

    day = request.session.get('day')
    guests = request.session.get('guests')
    First_name = request.session.get('First_name')
    Last_name = request.session.get('Last_name')
    Email = request.session.get('Email')
    Phone = request.session.get('Phone')
    
    #Only show the time of the day that has not been selected before and the time he is editing:
    hour = checkEditTime(times, day, id)
    appointment = Appointment.objects.get(pk=id)
    userSelectedTime = appointment.time
    if request.method == 'POST':
        time = request.POST.get("time")
        date = dayToWeekday(day)

        if guests != None:
            if day <= maxDate and day >= minDate:
                if date == 'Monday' or date == 'Saturday' or date == 'Wednesday':
                    if Appointment.objects.filter(day=day).count() < 11:
                        if Appointment.objects.filter(day=day, time=time).count() < 1 or userSelectedTime == time:
                            AppointmentForm = Appointment.objects.filter(pk=id).update(
                                user = user,
                                guests = guests,
                                First_name=First_name,
                                Last_name=Last_name,
                                Email=Email,
                                Phone=Phone,
                                day = day,
                                time = time,
                            ) 
                            messages.success(request, "Appointment Edited!")
                            return redirect('index')
                        else:
                            messages.success(request, "The Selected Time Has Been Reserved Before!")
                    else:
                        messages.success(request, "The Selected Day Is Full!")
                else:
                    messages.success(request, "The Selected Date Is Incorrect")
            else:
                    messages.success(request, "The Selected Date Isn't In The Correct Time Period!")
        else:
            messages.success(request, "Your booking is saved!")
        return redirect('userPanel')


    return render(request, 'userUpdateSubmit.html', {
        'times':hour,
        'id': id,
    })

def staffPanel(request):
    today = datetime.today()
    minDate = today.strftime('%Y-%m-%d')
    deltatime = today + timedelta(days=21)
    strdeltatime = deltatime.strftime('%Y-%m-%d')
    maxDate = strdeltatime
    #Only show the Appointments 21 days from today
    items = Appointment.objects.filter(day__range=[minDate, maxDate]).order_by('day', 'time')

    return render(request, 'staffPanel.html', {
        'items':items,
    })

def dayToWeekday(x):
    z = datetime.strptime(x, "%Y-%m-%d")
    y = z.strftime('%A')
    return y

def validWeekday(days):
    #Loop days you want in the next 21 days:
    today = datetime.now()
    weekdays = []
    for i in range (0, days):
        x = today + timedelta(days=i)
        y = x.strftime('%A')
        if y == 'Monday' or y == 'Saturday' or y == 'Wednesday':
            weekdays.append(x.strftime('%Y-%m-%d'))
    return weekdays
    
def isWeekdayValid(x):
    validateWeekdays = []
    for j in x:
        if Appointment.objects.filter(day=j).count() < 10:
            validateWeekdays.append(j)
    return validateWeekdays

def checkTime(times, day):
    #Only show the time of the day that has not been selected before:
    x = []
    for k in times:
        if Appointment.objects.filter(day=day, time=k).count() < 1:
            x.append(k)
    return x

def checkEditTime(times, day, id):
    #Only show the time of the day that has not been selected before:
    x = []
    appointment = Appointment.objects.get(pk=id)
    time = appointment.time
    for k in times:
        if Appointment.objects.filter(day=day, time=k).count() < 1 or time == k:
            x.append(k)
    return x
# Create your views here.
