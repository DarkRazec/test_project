from django.db import models

from companies.models import Company, NULLABLE


class Product(models.Model):
    name = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    release_date = models.DateField()
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, **NULLABLE)

    def __str__(self):
        return f"{self.name} ({self.model})"
