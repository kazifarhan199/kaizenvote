from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
class Title_model(models.Model):
	user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
	title = models.CharField(max_length=400)
	discription = models.CharField(max_length=20000)

	def __str__(self):
		return str(self.title)
