from django.urls import path
from .views import *

urlpatterns = [
	path('', index, name="index"),
	path('staff/', staff, name="staff"),
]
