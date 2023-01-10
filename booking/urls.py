from django.urls import path 
from . import views
from booking.views import index, about, contact, menu, bookingpage

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.about, name='about'),
    path('', views.contact, name='contact'),
    path('', views.menu, name='menu'),
    path('', views.bookingpage, name='bookingpage'),
    path('booking', views.booking, name='booking'),
    path('booking-submit', views.bookingSubmit, name='bookingSubmit'),
]