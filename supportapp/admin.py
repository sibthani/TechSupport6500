from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import *
from .models import *



admin.site.register(Cluster)
admin.site.register(Center)
admin.site.register(Staff)
admin.site.register(Issue)
admin.site.register(Issue_Catgry)

class CustomUserAdmin(UserAdmin):
    model = CoachUser
    list_display = ('username','first_name', 'is_staff', 'is_active',)
    list_filter = ('username','first_name','is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('username','email', 'first_name','last_name','password','country_code'
        ,'cluster_code','center_code','coach_career','address','phone_number','groups')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username','password1','password2','email', 
            'first_name','last_name','gender','phone_number','cluster_code','center_code',
            'staff_code',
            'is_staff', 'is_active')}
        ),
    )
    search_fields = ('username',)
    ordering = ('username',)

admin.site.register(CoachUser, CustomUserAdmin)