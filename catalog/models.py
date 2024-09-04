from django.db import models
from datetime import date


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Наименование категории",
        help_text="Введите наименование категории"
    )
    description = models.TextField(
        verbose_name='Описание категории',
        help_text='Введите описание категории',
        blank=True,
        null=True
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
        help_text="Введите наименование товара"
    )
    description = models.TextField(
        verbose_name='Описание товара',
        help_text='Введите описание товара',
        blank=True,
        null=True
    )
    photo = models.ImageField(
        verbose_name='Изображение',
        help_text='Загрузите фото товара',
        blank=True,
        null=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name = 'Категория',
        help_text = 'Введите категорию товара',
        blank=True,
        null=True,
        related_name='category'
    )
    price = models.IntegerField(
        verbose_name = 'Цена',
        help_text = 'Введите цену'
    )
    created_at = models.DateField(
        verbose_name='Дата создания записи'
    )
    updated_at = models.DateField(
        verbose_name='Дата последнего изменения записи'
    )
    manufactured_at = models.DateField(
        default=date(2001, 6, 23),
        verbose_name='Дата производства продукта'
    )


    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.name



