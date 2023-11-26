from django.shortcuts import render
from .models import ControlLED
import serial

# Create your views here.
def control_led(request):
    led_status = ControlLED.objects.first().led_status

    if request.method == 'POST':
        arduino = serial.Serial('COM3', 115200, timeout=1)
        arduino.write(b'1')
        arduino.close()

        ControlLED.objects.first().led_status = not led_status
        ControlLED.objects.first().save()
        led_status = not led_status

    return render(request, 'control_led.html', {'led_status': led_status})
