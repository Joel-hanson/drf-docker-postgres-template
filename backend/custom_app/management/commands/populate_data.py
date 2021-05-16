from django.core.management.base import BaseCommand
from ...models import Team, Product


class Command(BaseCommand):
    help = "Create the initial data required to run the project"

    def handle(self, *args, **options):
        # Create products
        products = [
            {"category": 1, "model_no": "T2020UHD", "available": 1, "price": 3899},
            {"category": 1, "model_no": "T20214K", "available": 3, "price": 45499},
            {"category": 2, "model_no": "R260LCS", "available": 0, "price": 21449},
            {"category": 2, "model_no": "R395LIL", "available": 2, "price": 35999}
        ]
        create_list = [ Product(**row) for row in products ]
        try:
            Product.objects.bulk_create(create_list)
        except:
            print("products already exists")

        # Create team
        teams = [
            {"team_name": "Team A"},
            {"team_name": "Team B"},
        ]
        create_list = [ Team(**row) for row in teams ]
        try:
            Team.objects.bulk_create(create_list)
        except:
            print("teams already exists")
        print("populated")
