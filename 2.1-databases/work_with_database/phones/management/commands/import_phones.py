import csv

from django.core.management.base import BaseCommand
from phones.models import Phone
from django.utils.text import slugify


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            item = Phone(
                phone['id'],
                phone['name'],
                phone['price'],
                phone['image'],
                phone['release_date'],
                phone['lte_exists'],
                slugify(phone['name']))
            item.save()
