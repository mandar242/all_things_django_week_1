from django import forms
from .models import Mamtak


class MamtakForm(forms.ModelForm):
    class Meta:
        model = Mamtak
        fields = ['name', 'buyer', 'description', 'flavour', 'purchase_date','ingredients']

'''

    CHOC_CHOICES = [('W', 'White'),('M', 'Milk'),('D','Dark'),('R','Ruby')]
    name = models.CharField(max_length=100)
    buyer = models.CharField(max_length=100)
    description = models.TextField()
    flavour = models.CharField(max_length=1, choices=CHOC_CHOICES, blank=True)
    purchase_date = models.DateTimeField()
    ingredients = models.ManyToManyField('Ingredients', blank=True)

'''