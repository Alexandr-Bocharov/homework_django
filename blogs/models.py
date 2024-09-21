from django.db import models
from django.db.models import ImageField


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='заголовок')
    slug = models.CharField(max_length=150, unique=True, null=True, blank=True, verbose_name='Slug')
    body = models.TextField(verbose_name='содержимое')
    photo = ImageField(verbose_name='превью', null=True, blank=True)
    created_at = models.DateField(auto_now_add=True, verbose_name='дата создания', null=True, blank=True)
    public_sign = models.BooleanField(default=False, verbose_name='признак публикации')
    views_count = models.IntegerField(default=0, verbose_name='счетчик просмотров')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
        ordering = ['-created_at']


