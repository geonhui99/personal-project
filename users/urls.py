from django.urls import path
from django.http import JsonResponse

def ping(_request):
    return JsonResponse({"users": "pong"})

urlpatterns = [
    path('ping/', ping, name='users-ping'),
]
