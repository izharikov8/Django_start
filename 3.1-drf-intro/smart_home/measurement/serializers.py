from rest_framework import serializers
from measurement.models import Sensor, Measurement
# TODO: опишите необходимые сериализаторы


class SensorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Sensor
		fields = ['name', 'description']


class MeasurementSerializer(serializers.ModelSerializer):
	class Meta:
		model = Measurement
		fields = ['date', 'temp']


class SensorDetailSerializer(serializers.ModelSerializer):
	measurements = MeasurementSerializer(read_only=True, many=True)

	class Meta:
		model = Sensor
		fields = ['id', 'name', 'description', 'measurements']