from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)


class Sensor(models.Model):
	name = models.CharField(max_length=50)
	description = models.CharField(max_length=256)


class Measurement(models.Model):
	sensor_id = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
	temp = models.DecimalField(max_digits=5, decimal_places=1)
	date = models.DateTimeField(auto_now_add=True, blank=True)
