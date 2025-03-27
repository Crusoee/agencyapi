import json
import requests
from app.models import Agency

data = requests.get("https://www.ecfr.gov/api/admin/v1/agencies").json()

for item in data:
    Agency.objects.create(
        name=item["name"],
        short_name=item["short_name"],
        display_name=item["display_name"],
        sortable_name=item["sortable_name"],
        slug=item["slug"],
        children=json.dumps(item["children"]),
        cfr_references=json.dumps(item["cfr_references"])
    )