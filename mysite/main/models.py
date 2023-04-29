from django.db import models

# Create your models here.
class Shoe(models.Model):

    name = models.CharField('Shoe name', max_length=100)
    price = models.PositiveIntegerField('Shoe price')
    img = models.ImageField('Shoe image', upload_to='home')
    video = models.FileField('Shoe video')

    def __str__(self):
        return self.name