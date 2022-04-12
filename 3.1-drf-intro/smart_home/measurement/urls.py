from django.urls import path
from measurement.views import SensorView, SensorsView, SensorCreate, SensorUpdate, MeasurementView, SensorDataView, MeasurementCheck

urlpatterns = [
	path('sensors/', SensorsView.as_view()),
	path('sensor/<pk>/', SensorView.as_view()),
	path('new_sensor/', SensorCreate.as_view()),
	path('update_sensor/<pk>/', SensorUpdate.as_view()),
	path('measurements/', MeasurementView.as_view()),
	path('sensor_data/<pk>/', SensorDataView.as_view()),
	path('measure_check/', MeasurementCheck.as_view())
]
