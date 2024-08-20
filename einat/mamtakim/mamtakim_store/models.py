from django.db import models

# Create your models here.
class Mamtak(models.Model):

    CHOC_CHOICES = [('W', 'White'),('M', 'Milk'),('D','Dark'),('R','Ruby')]
    name = models.CharField(max_length=100)
    buyer = models.CharField(max_length=100)
    description = models.TextField()
    flavour = models.CharField(max_length=1, choices=CHOC_CHOICES, blank=True)
    purchase_date = models.DateTimeField()
    ingredients = models.ManyToManyField('Ingredients', blank=True)

class Ingredients(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
