from django import forms
from .models import Order, Product, ProductCategory


class ProductForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = ['name', 'category', 'quantity']


class ProductCategoryForm(forms.ModelForm):
	class Meta:
		model = ProductCategory
		fields = '__all__'

class OrderForm(forms.ModelForm):
	class Meta:
		model = Order
		fields = ['product', 'order_quantity']
