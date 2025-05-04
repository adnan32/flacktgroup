from django.db import models
from django.core.validators import RegexValidator

class Product(models.Model):
    name = models.CharField(max_length=100)
    part_number = models.CharField(
        max_length=10,
        unique=True,
        validators=[RegexValidator(r'^[A-Za-z0-9]{6,10}$', 'Part number must be 6-10 alphanumeric characters')]
    )
    size_mm = models.PositiveIntegerField()
    color = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} ({self.part_number})"
