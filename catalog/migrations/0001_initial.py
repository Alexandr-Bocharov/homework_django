# Generated by Django 5.1 on 2024-09-04 14:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Введите наименование категории",
                        max_length=100,
                        verbose_name="Наименование категории",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        help_text="Введите описание категории",
                        null=True,
                        verbose_name="Описание категории",
                    ),
                ),
            ],
            options={
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Введите наименование товара",
                        max_length=100,
                        verbose_name="Наименование товара",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        help_text="Введите описание товара",
                        null=True,
                        verbose_name="Описание товара",
                    ),
                ),
                (
                    "photo",
                    models.ImageField(
                        blank=True,
                        help_text="Загрузите фото товара",
                        null=True,
                        upload_to="",
                        verbose_name="Изображение",
                    ),
                ),
                (
                    "price",
                    models.IntegerField(help_text="Введите цену", verbose_name="Цена"),
                ),
                ("created_at", models.DateField(verbose_name="Дата создания записи")),
                (
                    "updated_at",
                    models.DateField(verbose_name="Дата последнего изменения записи"),
                ),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        help_text="Введите категорию товара",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="category",
                        to="catalog.category",
                        verbose_name="Категория",
                    ),
                ),
            ],
            options={
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
            },
        ),
    ]
