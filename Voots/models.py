from django.db import models

class Voots_model(models.Model):
	ip = models.CharField(max_length=45)

	def __str__(self):
		return str(self.ip)
