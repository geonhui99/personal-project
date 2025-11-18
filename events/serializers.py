from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    booking_count = serializers.IntegerField(read_only=True)
    seats_sum = serializers.IntegerField(read_only=True)

    class Meta:
        model = Event
        fields = "__all__"

    def validate(self, data):
        start = data.get("start_at") or getattr(self.instance, "start_at", None)
        end = data.get("end_at") or getattr(self.instance, "end_at", None)
        if start and end and end <= start:
            raise serializers.ValidationError("end_at은 start_at 보다 늦어야 합니다.")
        return data
