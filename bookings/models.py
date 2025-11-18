from django.db import models
from events.models import Event

class Booking(models.Model):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    CANCELED = "canceled"
    STATUS_CHOICES = [
        (PENDING, "Pending"),
        (CONFIRMED, "Confirmed"),
        (CANCELED, "Canceled"),
    ]

    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="bookings")
    name = models.CharField(max_length=100)
    seats = models.PositiveIntegerField(default=1)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=PENDING)
    booked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"[{self.get_status_display()}] {self.name} x{self.seats} -> {self.event}"
