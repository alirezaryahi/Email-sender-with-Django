from django.contrib import admin
from .models import ContactUs


# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'is_read']
    list_filter = ('is_read',)

    class Meta:
        model = ContactUs


admin.site.register(ContactUs, ContactAdmin)
