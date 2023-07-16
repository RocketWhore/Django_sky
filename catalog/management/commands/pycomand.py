from django.core.management import BaseCommand

from catalog.models import *

class Command(BaseCommand):
    def handle(self, *args, **options):
        product_list = [
            {
                    "title": "Orange",
                    "description": "orange, sweet",
                    "avatar": "catalog/���_�����.png",
                    "category_id": 1,
                    "price": 100,
                    "date_of_born": "2023-07-16T13:10:39.751Z",
                    "date_of_change": "2023-07-16T13:10:39.751Z"
                },
            {'title': 'coconut', 'description': 'white', 'category_id': '1', 'price': '100'},
            {'title': 'cucumber', 'description': 'green', 'category_id': '2', 'price': '100'}

        ]
        product_to_create = []
        for i in product_list:
            product_to_create.append(
                Product(**i)
            )
        Product.objects.bulk_create(product_to_create)
        # Product.objects.create(**product_list[0])