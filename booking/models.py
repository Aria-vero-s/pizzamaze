from django.db import models
from django import forms
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from datetime import datetime
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

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


class RegisterUserForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class Table(models.Model):
    first_name = models.ForeignKey(RegisterUserForm, blank=True, null=True, on_delete=models.CASCADE)
    last_name = models.ForeignKey(RegisterUserForm, blank=True, null=True, on_delete=models.CASCADE)
    email = models.ForeignKey(RegisterUserForm, blank=True, null=True, on_delete=models.CASCADE)
    phone = models.ForeignKey(RegisterUserForm, blank=True, null=True, on_delete=models.CASCADE)
    guests = models.CharField(max_length=50, choices=GUESTS, default="1 guest")
    day = models.DateField(default=datetime.now)
    time = models.CharField(max_length=10, choices=TIME_CHOICES, default="3 PM")
    time_ordered = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return f"day: {self.day} | time: {self.time}"
