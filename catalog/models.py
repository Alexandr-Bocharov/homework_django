from django.db import models
from datetime import date

from users.models import User, NULLABLE


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Наименование категории",
        help_text="Введите наименование категории",
    )
    description = models.TextField(
        verbose_name="Описание категории",
        help_text="Введите описание категории",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Наименование товара",
    )
    description = models.TextField(
        verbose_name="Описание товара",
        blank=True,
        null=True,
    )
    photo = models.ImageField(
        verbose_name="Изображение",
        blank=True,
        null=True,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        blank=True,
        null=True,
        related_name="category",
    )
    price = models.IntegerField(verbose_name="Цена")
    created_at = models.DateField(
        verbose_name="Дата создания записи", blank=True, null=True
    )
    updated_at = models.DateField(
        verbose_name="Дата последнего изменения записи", blank=True, null=True
    )
    salesman = models.ForeignKey(User, verbose_name='продавец', on_delete=models.SET_NULL, **NULLABLE)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ("-id",)

    def __str__(self):
        return self.name


class Contacts(models.Model):
    address = models.CharField(
        max_length=250, verbose_name="Адрес", help_text="Введите адрес"
    )
    inn = models.CharField(
        max_length=100,
        verbose_name="ИНН",
        help_text="Введите ИНН",
        blank=True,
        null=True,
    )
    country = models.CharField(
        max_length=50, verbose_name="Страна", help_text="Введите страну"
    )

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"

    def __str__(self):
        return self.inn


class Version(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="product",
        verbose_name="продукт",
    )
    version_number = models.IntegerField(
        verbose_name='номер версии',
    )
    version_name = models.CharField(
        max_length=100,
        verbose_name='название версии',
    )
    current_version_flag = models.BooleanField(
        verbose_name='признак текущей версии',
    )

    def __str__(self):
        return self.version_name

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'