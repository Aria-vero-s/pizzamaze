from django.urls import path, include
from . import views
from booking.views import index, about, contact, feedback, menu, booking, bookingSubmit, login, register_user, venue
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
    path('logout', views.logout_user, name="logout"),
    path('register_user', views.register_user, name="register_user"),
    path('venue', views.venue, name="venue"),
    path('list_venues', views.list_venues, name="add-venue"),
    path('show_venue/<venue_id>', views.show_venue, name='show-venue'),
    path('update_venue/<venue_id>', views.update_venue, name='update-venue'),
]