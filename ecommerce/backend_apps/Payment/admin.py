from django.contrib import admin
from .models import PaymentType, UserPaymentMethod

# Register your models here.

@admin.register(PaymentType)
class PaymentTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    list_per_page = 20

@admin.register(UserPaymentMethod)
class UserPaymentMethodAdmin(admin.ModelAdmin):
    list_display = ('user', 'payment_type', 'payment_info', 'is_default')
    list_filter = ('user', 'payment_type', 'is_default')
    search_fields = ('user__username', 'payment_type__name', 'payment_info')
    list_per_page = 20
