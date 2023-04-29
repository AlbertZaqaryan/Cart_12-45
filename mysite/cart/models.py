from django.db import models
from main.models import Shoe
# Create your models here.


class Cart(models.Model):

    prod = models.ForeignKey(Shoe, on_delete=models.CASCADE)