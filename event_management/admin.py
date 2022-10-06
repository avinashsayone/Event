from multiprocessing import Event
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import Addevent, CustomUserCreationForm, CustomUserChangeForm
from .models import User,Event
# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ['username','first_name','last_name','email']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ['phone_number', 'age','address']}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ['phone_number', 'age','address']}),
    )

admin.site.register(User, CustomUserAdmin)
admin.site.register(Event)