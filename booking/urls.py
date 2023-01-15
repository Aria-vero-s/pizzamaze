from django.urls import path 
from . import views
from booking.views import index, about, contact, menu, booking, bookingSubmit, register, staffPanel, userPanel, userUpdate, userUpdateSubmit

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('menu', views.menu, name='menu'),
    path('booking', views.booking, name='booking'),
    path('booking-submit', views.bookingSubmit, name='bookingSubmit'),
    path('register', views.register, name='register'),
    path('staffPanel', views.staffPanel, name='staffPanel'),
    path('userPanel', views.userPanel, name='userPanel'),
    path('userUpdate', views.userUpdate, name='userUpdate'),
    path('userUpdateSubmit', views.userUpdateSubmit, name='userUpdateSubmit'),
]