from Title.models import Title_model
from django.db import models

# Create your models here.
class Options_model(models.Model):
	title = models.ForeignKey(Title_model, on_delete=models.CASCADE)
	name = models.CharField(max_length=400)
	d1 = models.CharField(max_length=400, blank=True)
	d2 = models.CharField(max_length=400, blank=True)
	d3 = models.CharField(max_length=400, blank=True)
	votes = models.IntegerField(default=0)
	image = models.CharField(max_length=70000)
	url = models.TextField(default="https://www.flipkart.com/?affid=kazifarha")

	def __str__(self):
		return self.name
