from django.shortcuts import render, redirect
from datetime import datetime, timedelta
from .models import *
from django.contrib import messages
from django.urls import path
from . import views
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import RegisterUserForm
from .models import Table


def all_tables(request):
    table_list = Table.objects.all()
    return render(request, 'tables.html', {'table_list': table_list})


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
            return redirect('index')
    else:
        form = RegisterUserForm()
    return render(request, 'register_user.html', {'form': form, })


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
        # form.instance.login_user = author
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
        day = request.POST.get('day')
        guests = request.POST.get('guests')
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

        if GUESTS != None:
            if day <= maxDate and day >= minDate:
                if date == 'Monday' or date == 'Saturday' or date == 'Wednesday':
                    if Table.objects.filter(day=day).count() < 11:
                        if Table.objects.filter(day=day, time=time).count() < 1:
                            TableForm = Table.objects.get_or_create(
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


def userUpdate(request, id):
    table = Table.objects.get(pk=id)
    userdatepicked = table.day
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
    table = Table.objects.get(pk=id)
    userSelectedTime = table.time
    if request.method == 'POST':
        time = request.POST.get("time")
        date = dayToWeekday(day)

        if guests != None:
            if day <= maxDate and day >= minDate:
                if date == 'Monday' or date == 'Saturday' or date == 'Wednesday':
                    if Table.objects.filter(day=day).count() < 11:
                        if Table.objects.filter(day=day, time=time).count() < 1 or userSelectedTime == time:
                            TableForm = Table.objects.filter(pk=id).update(
                                user = user,
                                guests = guests,
                                First_name=First_name,
                                Last_name=Last_name,
                                Email=Email,
                                Phone=Phone,
                                day = day,
                                time = time,
                            ) 
                            messages.success(request, "Booking Edited!")
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
    #Only show the tables 21 days from today
    items = Table.objects.filter(day__range=[minDate, maxDate]).order_by('day', 'time')

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
        if Table.objects.filter(day=j).count() < 10:
            validateWeekdays.append(j)
    return validateWeekdays

def checkTime(times, day):
    #Only show the time of the day that has not been selected before:
    x = []
    for k in times:
        if Table.objects.filter(day=day, time=k).count() < 1:
            x.append(k)
    return x

def checkEditTime(times, day, id):
    #Only show the time of the day that has not been selected before:
    x = []
    table = Table.objects.get(pk=id)
    time = table.time
    for k in times:
        if Table.objects.filter(day=day, time=k).count() < 1 or time == k:
            x.append(k)
    return x
# Create your views here.
