from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("id", "event", "name", "seats", "status", "booked_at")
    list_filter = ("status", "event")
    search_fields = ("name",)
    autocomplete_fields = ("event",)
    ordering = ("-booked_at",)
    actions = ("mark_confirmed", "mark_canceled")

    def mark_confirmed(self, request, queryset):
        updated = queryset.update(status=Booking.CONFIRMED)
        self.message_user(request, f"{updated}건을 확정으로 변경했습니다.")

    mark_confirmed.short_description = "선택한 예약을 확정 처리"

    def mark_canceled(self, request, queryset):
        updated = queryset.update(status=Booking.CANCELED)
        self.message_user(request, f"{updated}건을 취소로 변경했습니다.")

    mark_canceled.short_description = "선택한 예약을 취소 처리"
