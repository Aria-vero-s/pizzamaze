from django.contrib import admin
from .models import *
from .models import Table
from .models import RegisterUserForm

admin.site.register(Table)
admin.site.register(RegisterUserForm)
