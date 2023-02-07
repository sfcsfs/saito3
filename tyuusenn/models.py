from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Device(models.Model):
    name = models.CharField(max_length=255)
    touhyou = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10000)])
    bikou = models.CharField(max_length=255)

    def __str__(self):
        return self.name
