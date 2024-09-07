import json
from django.core.management.base import BaseCommand
from django.db import connection
from catalog.models import Product, Category


class Command(BaseCommand):
    help = 'Загружает данные из JSON файлов'

    def handle(self, *args, **kwargs):
        # Удаление данных в правильном порядке
        Product.objects.all().delete()
        Category.objects.all().delete()

        with connection.cursor() as cursor:
            cursor.execute('ALTER SEQUENCE catalog_category_id_seq RESTART WITH 1')
            cursor.execute('ALTER SEQUENCE catalog_product_id_seq RESTART WITH 1')

        categories_for_create = []
        products_for_create = []

        with open('data/db_data_category.json') as file:
            categories_data = json.load(file)
            for item in categories_data:
                fields = item['fields']
                categories_for_create.append(Category(**fields))

        # Category.objects.bulk_create(categories_for_create)

        Category.objects.bulk_create(categories_for_create)

        with open('data/db_data_product.json') as file:
            products_data = json.load(file)
            for item in products_data:
                fields = item['fields']
                if 'category' in fields:
                    category_id = fields['category']
                    getting_object = Category.objects.get(pk=category_id)
                    fields['category'] = getting_object
                products_for_create.append(Product(**fields))

        Product.objects.bulk_create(products_for_create)
