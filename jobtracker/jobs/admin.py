from django.contrib import admin
from .models import Job, OTP


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'organization', 'category', 'last_date', 'status')
    list_filter = ('category', 'status')
    search_fields = ('title', 'organization')


@admin.register(OTP)
class OTPAdmin(admin.ModelAdmin):
    list_display = ('user', 'otp', 'created_at')

