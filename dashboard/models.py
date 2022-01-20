from sre_parse import CATEGORIES
from statistics import quantiles
from unicodedata import category
from django.db import models

# Create your models here.

CATEGORIES = (
	('stationary', 'stationary'),
	('Electronics', 'Electronics'),
	('Food', 'Food'),
)
class Product(models.Model):
	name = models.CharField(max_length=100, null=True)
	category = models.CharField(max_length=20, choices=CATEGORIES, null=True)
	quantity = models.PositiveIntegerField(null=True)

	class Meta:
		verbose_name = 'Product'
		verbose_name_plural = 'Products'

	def __str__(self):
		return self.name
