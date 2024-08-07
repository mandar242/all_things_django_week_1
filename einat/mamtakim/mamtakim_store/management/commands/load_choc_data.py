from csv import DictReader
from datetime import datetime

from django.core.management import BaseCommand

from mamtakim_store.models import Mamtak, Ingredients
from pytz import UTC


DATETIME_FORMAT = '%m/%d/%Y %H:%M'

INGREDIENTS_NAMES = [
    'milk',
    'cocoa',
    'sugar',
    'milk chocolate bar flavouring',
    'dark chocolate bar flavouring',
    'white chocolate bar flavouring',
    'ruby chocolate bar flavouring',
    'pop stick',
    'strawberries',
    'lemons',
    'coconut'
]

ALREADY_LOADED_ERROR_MESSAGE = """
If you need to reload the mamtak data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from mamtak.csv into our Mamtak mode"

    def handle(self, *args, **options):
        if Mamtak.objects.exists() or Ingredients.objects.exists():
            print('Mamtak data already loaded...exiting.')
            print(ALREADY_LOADED_ERROR_MESSAGE)
            return
        print("Creating mamtak data")
        for Ingredients_name in INGREDIENTS_NAMES:
            ing = Ingredients(name=Ingredients_name)
            ing.save()
        print("Loading mamtak data for mamtakim available for purchase")
        for row in DictReader(open('./mamtak.csv')):
            mamtak = Mamtak()
            mamtak.name = row['Name']
            mamtak.buyer = row['Buyer']
            mamtak.description = row['Description']
            mamtak.flavour = row['Flavour']
            raw_purchase_date = row['Purchase_date']
            purchase_date = UTC.localize(
                datetime.strptime(raw_purchase_date, DATETIME_FORMAT))
            mamtak.purchase_date = purchase_date
            mamtak.save()
            raw_ingredients_names = row['Ingredients']
            ingredients_names = [name for name in raw_ingredients_names.split('| ') if name]
            for ing_name in ingredients_names:
                ing = Ingredients.objects.get(name=ing_name)
                mamtak.ingredients.add(ing)
            mamtak.save()
