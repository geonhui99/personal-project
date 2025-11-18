from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Booking
from .serializers import BookingSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.select_related("event").all().order_by("-booked_at")
    serializer_class = BookingSerializer
    # 읽기는 허용, 생성/수정/삭제/상태변경은 인증 필요
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # 검색/정렬/필터
    search_fields = ["name"]
    ordering_fields = ["booked_at", "seats"]
    filterset_fields = ["status", "event"]

    @action(detail=True, methods=["post"], url_path="confirm")
    def confirm(self, request, pk=None):
        booking = self.get_object()
        if booking.status == Booking.CONFIRMED:
            return Response({"detail": "이미 확정 상태입니다."}, status=status.HTTP_400_BAD_REQUEST)
        booking.status = Booking.CONFIRMED
        booking.save(update_fields=["status"])
        return Response(BookingSerializer(booking).data, status=status.HTTP_200_OK)

    @action(detail=True, methods=["post"], url_path="cancel")
    def cancel(self, request, pk=None):
        booking = self.get_object()
        if booking.status == Booking.CANCELED:
            return Response({"detail": "이미 취소 상태입니다."}, status=status.HTTP_400_BAD_REQUEST)
        booking.status = Booking.CANCELED
        booking.save(update_fields=["status"])
        return Response(BookingSerializer(booking).data, status=status.HTTP_200_OK)
