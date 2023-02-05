from django.db import models
from django import forms
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from datetime import datetime

GUESTS = (
    ("1 guest", "1 guest"),
    ("2 guests", "2 guests"),
    ("3 guests", "3 guests"),
    ("4 guests", "4 guests"),
    ("5 guests", "5 guests"),
    ("6 guests", "6 guests"),
    ("7 guests", "7 guests"),
    ("8 guests", "8 guests"),
    )
TIME_CHOICES = (
    ("9 AM", "9 AM"),
    ("10 AM", "10 AM"),
    ("11 AM", "11 AM"),
    ("12 PM", "12 PM"),
    ("1 PM", "1 PM"),
    ("2 PM", "2 PM"),
    ("3 PM", "3 PM"),
    ("4 PM", "4 PM"),
    ("5 PM", "5 PM"),
    ("6 PM", "6 PM"),
    ("7 PM", "7 PM"),
    ("8 PM", "8 PM"),
    ("9 PM", "9 PM"),
)

class Table(models.Model):
    guests = models.CharField(max_length=50, choices=GUESTS, default="1 guest")
    First_name = models.CharField(max_length=20, help_text='First name')
    Last_name = models.CharField(max_length=20, help_text='Last name')
    Email = models.EmailField(max_length=20, help_text='Email')
    Phone = models.CharField(max_length=20, help_text='Phone')
    day = models.DateField(default=datetime.now)
    time = models.CharField(max_length=10, choices=TIME_CHOICES, default="3 PM")
    time_ordered = models.DateTimeField(default=datetime.now, blank=True)
    address = forms.CharField(max_length=200)
    def __str__(self):
        return f"day: {self.day} | time: {self.time}"


class Venue(models.Model):
    name = models.CharField('Venue Name', max_length=120)
    address = models.CharField(max_length=300)
    zip_code = models.CharField('Zip Code', max_length=15)
    phone = models.CharField('Contact Phone', max_length=25, blank=True)
    web = models.URLField('Website Address', blank=True)
    email_address = models.EmailField('Email Address', blank=True)
    owner = models.IntegerField("Venue Owner", blank=False, default=1)
    venue_image = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.name
