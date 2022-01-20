from django.urls import path
from .views import *

urlpatterns = [
	path('dashboard/', index, name="dashboard-index"),
	path('staff/', staff, name="dashboard-staff"),
	path('product/', product, name="dashboard-product"),
	path('order/', order, name="dashboard-order"),
]
