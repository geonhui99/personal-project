from rest_framework import viewsets, permissions
from django.db.models import Count, Sum
from django.db.models.functions import Coalesce
from .models import Event
from .serializers import EventSerializer

class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields = ["title", "description", "location"]
    ordering_fields = ["start_at", "title", "created_at"]
    filterset_fields = ["location"]

    def get_queryset(self):
        return (
            Event.objects
            .annotate(
                booking_count=Count("bookings"),
                seats_sum=Coalesce(Sum("bookings__seats"), 0),
            )
            .order_by("-start_at")
        )
