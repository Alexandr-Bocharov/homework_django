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

        # Сброс последовательностей для автоинкрементных полей
        with connection.cursor() as cursor:
            cursor.execute('ALTER SEQUENCE catalog_category_id_seq RESTART WITH 1')
            cursor.execute('ALTER SEQUENCE catalog_product_id_seq RESTART WITH 1')

        # Загрузка данных категорий
        self.stdout.write(self.style.NOTICE('Загрузка данных категорий...'))
        category_mapping = {}
        with open('data/db_data_category.json') as file:
            categories_data = json.load(file)
            for item in categories_data:
                fields = item['fields']
                category = Category.objects.create(**fields)
                category_mapping[category.pk] = category

        # Загрузка данных продуктов
        self.stdout.write(self.style.NOTICE('Загрузка данных продуктов...'))
        with open('data/db_data_product.json') as file:
            products_data = json.load(file)
            for item in products_data:
                fields = item['fields']
                # Замена ID категории на объект Category
                if 'category' in fields:
                    category_id = fields['category']
                    getting_object = Category.objects.get(pk=category_id)
                    if category_id in category_mapping:
                        fields['category'] = getting_object
                Product.objects.create(**fields)

        self.stdout.write(self.style.SUCCESS('Данные успешно загружены!'))









# from django.core.management import BaseCommand
# import json
# from catalog.models import Product, Category
#
#
#
# class Command(BaseCommand):
#
#     def handle(self, *args, **options):
#         Product.objects.all().delete()
#         Category.objects.all().delete()
#
#         products = []
#         categories = []
#
#         with open('data/db_data.json') as file:
#             info = json.load(file)
#             for line in info:
#                 if 'category' in line['model']:
#                     categories.append(line)
#                 elif 'product' in line['model']:
#                     products.append(line)
#
#         # print(*products, sep='\n')
#         # print(*categories, sep='\n')
#
#         products_for_create = []
#         categories_for_create = []
#
#         for line in categories:
#             categories_for_create.append(
#                 Category(**line['fields'])
#             )
#
#         for line in products:
#             if line['fields']['category'] == 6:
#                 line['fields']['category'] = Category.objects.get(name='Обучение')
#             if line['fields']['category'] == 7:
#                 line['fields']['category'] = Category.objects.get(name='Мерч')
#             products_for_create.append(
#                 Product(**line['fields'])
#             )




        # for line in products_for_create:
        #     print(line.__dict__)
        #
        # for line in categories_for_create:
        #     print(line.__dict__)

        # Category.objects.bulk_create(categories_for_create)
        # Product.objects.bulk_create(products_for_create)
