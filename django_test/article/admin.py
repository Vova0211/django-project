from django.contrib import admin
from django.contrib.admin import DateFieldListFilter

from .models import Card

class CardAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at')
    search_fields = ['title', 'body', 'price']
    list_filter = (
        ("created_at", DateFieldListFilter),
        ("updated_at", DateFieldListFilter),
    )

admin.site.register(Card, CardAdmin)
