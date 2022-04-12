# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView


class SensorsView(ListAPIView):
	queryset = Sensor.objects.all()
	serializer_class = SensorSerializer


class SensorView(RetrieveAPIView):
	queryset = Sensor.objects.all()
	serializer_class = SensorSerializer


class SensorCreate(CreateAPIView):
	serializer_class = SensorSerializer


class SensorUpdate(UpdateAPIView):
	queryset = Sensor.objects.all()
	serializer_class = SensorSerializer


class MeasurementView(CreateAPIView):
	serializer_class = MeasurementSerializer


class SensorDataView(RetrieveAPIView):
	queryset = Sensor.objects.all()
	serializer_class = SensorDetailSerializer


class MeasurementCheck(ListAPIView):
	queryset = Measurement.objects.all()
	serializer_class = MeasurementSerializer
