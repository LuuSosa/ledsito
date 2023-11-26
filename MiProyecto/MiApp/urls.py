from django.urls import path
from .views import control_led

urlpatterns = [
    path('control_led', control_led, name='control_led'),
]