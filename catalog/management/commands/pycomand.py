from django.core.management import BaseCommand

from catalog.models import *

class Command(BaseCommand):
    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()
        category_list = [
            {
                    "title": "fruit",
                    "description": "sweet",

                },
            {'title': 'vegetables', 'description': 'not sweet', },
            {'title': 'electronics', 'description': 'Phones, PC', }

        ]
        category_to_create = []
        for i in category_list:
            category_to_create.append(
                Product(**i)
            )
        Category.objects.bulk_create(category_to_create)
        # Product.objects.create(**product_list[0])