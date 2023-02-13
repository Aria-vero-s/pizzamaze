from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('feedback', views.feedback, name='feedback'),
    path('menu', views.menu, name='menu'),
    path('booking', views.booking, name='booking'),
    path('login', views.login_user, name="login"),
    path('register_user', views.register_user, name="register_user"),
    path('notRegistered', views.notRegistered, name="notRegistered"),
    path('account', views.account, name="account"),
    path('edit/<booking_id>', views.bookingEdit, name='edit'),
    path('delete/<booking_id>', views.bookingDelete, name='delete'),
]
