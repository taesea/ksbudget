from django.db import models
from django.forms import ModelForm

class Expense(models.Model):
	expType = models.CharField(max_length = 20)
	expName = models.CharField(max_length = 20)
	expCost = models.DecimalField(decimal_places= 2, max_digits= 15)

	class Meta:
		abstract = True

class FoodExpense(Expense):
	expDate = models.DateField()

	def __str__(self):
		return self.question

class UserBudget(models.Model):
	monthTotalCost = models.DecimalField(decimal_places= 2, max_digits= 15)
	yearTotalCost = models.DecimalField(decimal_places= 2, max_digits= 15)

	def __str__(self):
		return self.question

class FoodExpenseForm(ModelForm):
	class Meta:
		model = FoodExpense
		fields = ['expDate', 'expType', 'expName', 'expCost']

