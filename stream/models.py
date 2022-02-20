from django.db import models


class FinanceLog(models.Model):

	currency = models.CharField(max_length=200)
	rate = models.IntegerField(default=0)


	def __str__(self):
		return self.currency
