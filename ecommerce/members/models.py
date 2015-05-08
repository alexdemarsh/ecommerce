from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()
	price = models.DecimalField(max_digits=6, decimal_places=2)

	def __unicode__(self):
		return self.name

class Order(models.Model):
	status = models.IntegerField()
	items = models.ManyToManyField(Item)
	user = models.ForeignKey(User)