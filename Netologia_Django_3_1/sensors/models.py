from django.db import models

class Sensor(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=512, blank=True)

    def __str__(self):
        return self.name


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, related_name='measurements', on_delete=models.CASCADE)
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True, upload_to='images/')

    def __str__(self):
        return f"{self.temperature}°C at {self.created_at}"
