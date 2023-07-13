from django.core.management import BaseCommand

from catalog.models import Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        product_list = [
            {'title': 'banana', 'description': 'yellow', 'category': 'fruit', 'price': '100'},
            {'title': 'coconut', 'description': 'white', 'category': 'fruit', 'price': '100'},
            {'title': 'MSI', 'description': 'PC', 'category': 'electronics', 'price': '100'},
            {'title': 'cucumber', 'description': 'green', 'category': 'vegetables', 'price': '100'}

        ]
        product_to_create = []
        for i in product_list:
            product_to_create.append(
                Product(**i)
            )
        Product.objects.bulk_create(product_to_create)