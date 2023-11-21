from django.core.management.base import BaseCommand
import csv

from GIS_MTP.models import MyDynamicModel  # Import your dynamic model class

class Command(BaseCommand):
    help = 'Import data and create dynamic models'

    def handle(self, *args, **options):
        # Your code to read the CSV and create models goes here
        a={}
