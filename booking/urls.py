from django.urls import path, include
from . import views
from booking.views import index, about, contact, feedback, menu, booking, bookingSubmit, login
from booking import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('feedback', views.feedback, name='feedback'),
    path('menu', views.menu, name='menu'),
    path('booking', views.booking, name='booking'),
    path('booking-submit', views.bookingSubmit, name='bookingSubmit'),
    path('login', views.login_user, name="login"),
]