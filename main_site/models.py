from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name='Категория продуктов')
    slug = models.SlugField(max_length=200, db_index=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название блюда')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    slug = models.SlugField(max_length=200, db_index=True)
    description = models.TextField(blank=True, verbose_name='Описание блюда')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюдо'

    def __str__(self):
        return self.name
