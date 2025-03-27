import json
from django.core.management.base import BaseCommand
from app.models import Agency
import requests

class Command(BaseCommand):
    help = "Load JSON data into SQLite database"

    # def add_arguments(self, parser):
    #     parser.add_argument('json_file', type=str, help='Path to JSON file')

    def handle(self, *args, **kwargs):
        agencies = requests.get("https://www.ecfr.gov/api/admin/v1/agencies").json()

        # data = json.load(f)
        for agency in agencies['agencies']:

            Agency.objects.create(
                name=agency["name"],
                short_name=agency["short_name"],
                display_name=agency["display_name"],
                sortable_name=agency["sortable_name"],
                slug=agency["slug"],
                children= agency["children"],
                cfr_references= agency["cfr_references"],
            )
        self.stdout.write(self.style.SUCCESS('Data loaded successfully!'))
