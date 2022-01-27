from django.urls import path
from .views import *

urlpatterns = [
	path('dashboard/', index, name="dashboard-index"),
	
	path('staff/', staff, name="dashboard-staff"),
	path('staff/detail/<int:pk>/', staff_detail, name="dashboard-staff-detail"),

	path('order/', order, name="dashboard-order"),
	path('order/update/<int:pk>/', order_update, name="dashboard-order-update"),
	path('order/delete/<int:pk>/', order_delete, name="dashboard-order-delete"),

	path('product/', product, name="dashboard-product"),
	path('product/create', create_product_category, name="dashboard-product-create"),
	path('product/update/<int:pk>/', product_update, name="dashboard-product-update"),
	path('product/delete/<int:pk>/', product_delete, name="dashboard-product-delete"),

	path('product/category/all/', category, name="dashboard-product-categories"),
	path('product/category/update/<int:pk>', category_update, name="dashboard-product-category-update"),
	path('product/category/delete/<int:pk>', category_delete, name="dashboard-product-category-delete"),
]
