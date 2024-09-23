from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Company(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, verbose_name='company email')
    country = models.CharField(max_length=100, verbose_name='country')
    city = models.CharField(max_length=100, verbose_name='city')
    street = models.CharField(max_length=150, verbose_name='street')
    house_number = models.CharField(max_length=10, verbose_name='house number')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='creation date')
    supplier = models.ForeignKey('self', default=None, on_delete=models.PROTECT, **NULLABLE, verbose_name='company supplier')
    debt = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, **NULLABLE, verbose_name='company debt')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'
