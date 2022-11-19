from django.contrib import admin
from .models import MyUser
from django.contrib.auth.admin import UserAdmin
from django.forms import Textarea
from django.db import models

class UserAdminSettings(UserAdmin):
    model = MyUser

    list_filter = ('is_staff', 'is_active')
    list_display = ['id', 'username', 'email', 'is_active', 'is_staff', 'start_date']
    prepopulated_fields = {'slug': ('username',),}
    search_fields = ['username', 'email']
    ordering = ('-start_date',)
    fieldsets = (
        (None, {'fields': ('username', 'email', 'slug' )}),
        ('Pазрешения', {'fields': (('is_active', 'is_staff'), 'is_superuser')}),
        ('Персональная информация', {'fields': ('about',)}),
        ('Активности', {
            'classes': ('collapse',), 
            'fields': ('last_login', 'start_date',)
        }),
    )
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 20, 'cols': 60})},
    }
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'slug', 'password1', 'password2', 'is_active', 'is_staff',)
        }),
    )

   

    



admin.site.register(MyUser, UserAdminSettings)



