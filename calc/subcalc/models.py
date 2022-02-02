from django.db import models

# Create your models here.
class Addition(models.Model):
	num1 = models.IntegerField(max_length=200, null=True)
	num2 = models.IntegerField(max_length=200, null=True)
	num3 = models.IntegerField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	