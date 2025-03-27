import json
from django.core.management.base import BaseCommand
from app.models import Agency, CfrReference
import requests

class Command(BaseCommand):
    help = "Load JSON data into SQLite database"

    # def add_arguments(self, parser):
    #     parser.add_argument('json_file', type=str, help='Path to JSON file')

    def handle(self, *args, **kwargs):
        data = requests.get("https://www.ecfr.gov/api/admin/v1/agencies").json()

        for agency_data in data['agencies']:
            parent_cfrs = []
            for cfr in agency_data.get('cfr_references', []):
                cfr_obj, _ = CfrReference.objects.get_or_create(
                    title=cfr.get('title'),
                    chapter=cfr.get('chapter')
                )
                parent_cfrs.append(cfr_obj)

            parent_agency = Agency.objects.create(
                name=agency_data['name'],
                short_name=(agency_data.get('short_name') or '')[:10],
                display_name=agency_data.get('display_name', agency_data['name']),
                sortable_name=agency_data.get('sortable_name', agency_data['name']),
                slug=agency_data['slug'],
                parent=None  # No parent
            )

            parent_agency.cfr_references.set(parent_cfrs)

            for child_data in agency_data.get('children', []):
                child_cfrs = []
                for cfr in child_data.get('cfr_references', []):
                    cfr_obj, _ = CfrReference.objects.get_or_create(
                        title=cfr.get('title'),
                        chapter=cfr.get('chapter')
                    )
                    child_cfrs.append(cfr_obj)

                child_agency = Agency.objects.create(
                    name=child_data['name'],
                    short_name=(child_data.get('short_name')or'')[:10],
                    display_name=child_data.get('display_name', child_data['name']),
                    sortable_name=child_data.get('sortable_name', child_data['name']),
                    slug=child_data['slug'],
                    parent=parent_agency
                )
                child_agency.cfr_references.set(child_cfrs)

        self.stdout.write(self.style.SUCCESS('Data loaded successfully!'))
