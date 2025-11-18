from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "start_at", "end_at", "location")
    search_fields = ("title", "location")
    list_filter = ("start_at",)
    ordering = ("-start_at",)
