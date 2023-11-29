from django.db import models

# Create your models here.


class producto(models.Model):
    nombre = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    calorias = models.CharField(max_length=20)

    class Meta:
        db_table = 'Producto'
