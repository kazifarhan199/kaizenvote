from django.db import models
from Title.models import Title_model
from Options.models import Options_model

class Voots_model(models.Model):
	title = models.ForeignKey(Title_model, on_delete=models.CASCADE)
	ip = models.CharField(max_length=45)
	option = models.ForeignKey(Options_model, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.ip)

	def save(self, *args, **kwargs):
		self.option.votes += 1
		self.option.save()
		super(Voots_model, self).save(*args, **kwargs)