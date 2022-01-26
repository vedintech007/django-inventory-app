from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class ProductCategory(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

class Product(models.Model):
	name = models.CharField(max_length=100, null=True)
	category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, null=True)
	quantity = models.PositiveIntegerField(null=True)

	class Meta:
		verbose_name_plural = 'Products'

	def __str__(self):
		return f"{self.name}"


class Order(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
	staff = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	order_quantity = models.PositiveIntegerField(null=True)
	date_of_order = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = 'Orders'

	def __str__(self):
		return f"{self.product} - ordered by {self.staff.username} - on {self.date_of_order}"
