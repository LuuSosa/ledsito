from django.db import models
# Create your models here.
class ControlLED(models.Model):
    led_status = models.BooleanField(default=False)
