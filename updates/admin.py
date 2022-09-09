from django.contrib import admin
from .models import Update


class UpdateAdmin(admin.ModelAdmin):
    list_display  = ('item', 'date_added')
    search_fields = ['date_added', ]

admin.site.register(Update, UpdateAdmin)
