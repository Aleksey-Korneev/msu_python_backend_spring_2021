from django.db import models


class Expense(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=256)
    amount = models.PositiveIntegerField()
