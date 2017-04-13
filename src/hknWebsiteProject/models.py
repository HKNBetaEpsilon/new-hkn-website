from django.db import models 


class Payment(models.Model):
    company_name = models.CharField(max_length=100)
    representative_name = models.CharField(max_length=100)
    representative_email = models.CharField(max_length=100)
    purpose = models.TextField()
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    