from django.urls import path
from .views import *

urlpatterns = [
	path('dashboard/', index, name="dashboard-index"),
	
	path('staff/', staff, name="dashboard-staff"),
	path('staff/detail/<int:pk>/', staff_detail, name="dashboard-staff-detail"),

	path('product/', product, name="dashboard-product"),
	path('order/', order, name="dashboard-order"),

	path('product/delete/<int:pk>/', product_delete, name="dashboard-product-delete"),
	path('product/update/<int:pk>/', product_update, name="dashboard-product-update"),
]
