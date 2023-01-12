from django.urls import path 
from . import views
from booking.views import index, about, contact, menu, bookingpage

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('menu', views.menu, name='menu'),
    path('bookingpage', views.bookingpage, name='bookingpage'),
    path('booking', views.booking, name='booking'),
    path('booking-submit', views.bookingSubmit, name='bookingSubmit'),
]