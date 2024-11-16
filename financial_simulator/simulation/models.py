from django.db import models

# Create your models here.
from django.db import models

class Simulation(models.Model):
    name = models.CharField(max_length=100)
    start_year = models.IntegerField(default=2023)
    user_income = models.FloatField()
    user_expenses = models.FloatField()
    savings_rate = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

class Decision(models.Model):
    simulation = models.ForeignKey(Simulation, on_delete=models.CASCADE)
    year = models.IntegerField()
    investment = models.FloatField()
    expense_reduction = models.FloatField()
    savings = models.FloatField()

class Outcome(models.Model):
    simulation = models.ForeignKey(Simulation, on_delete=models.CASCADE)
    year = models.IntegerField()
    net_worth = models.FloatField()
    total_savings = models.FloatField()
    investment_return = models.FloatField()
