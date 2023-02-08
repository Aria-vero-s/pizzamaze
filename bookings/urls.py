from django.urls import path, include
from . import views

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
    path('account', views.account, name="account"),
    # path('tables', views.all_tables, name="list-tables"),
    path('edit/<item_id>', bookingEdit, name='edit'),
]
