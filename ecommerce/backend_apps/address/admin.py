from django.contrib import admin
from .models import Address,UserAddress


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('address_line_1', 'city', 'state', 'postal_code', 'country')
    list_filter = ('city', 'state', 'country')
    search_fields = ('address_line_1', 'address_line_2', 'city', 'state', 'postal_code', 'country')
    ordering = ('-id',)  # Example: Order by descending ID

    fieldsets = (
        ('Address Information', {
            'fields': ('house_number', 'land_mark', 'address_line_1', 'address_line_2')
        }),
        ('Location Information', {
            'fields': ('city', 'state', 'postal_code', 'country')
        }),
    )


@admin.register(UserAddress)
class UserAddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'is_default')
    list_filter = ('is_default',)
    search_fields = ('user__username', 'address__address_line_1', 'address__city', 'address__state', 'address__postal_code', 'address__country')
    ordering = ('-id',)  # Example: Order by descending ID

    fieldsets = (
        ('User Address Information', {
            'fields': ('user', 'address', 'is_default')
        }),
    )

