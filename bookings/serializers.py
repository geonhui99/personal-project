from rest_framework import serializers
from .models import Booking

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"

    def validate_seats(self, value):
        if value < 1:
            raise serializers.ValidationError("seats는 1 이상이어야 합니다.")
        return value
