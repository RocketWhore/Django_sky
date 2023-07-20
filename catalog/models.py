from django.db import models

# Create your models here
NULLABLE = {'blank':  True, 'null': True}
class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField()
    avatar = models.ImageField(upload_to='catalog/', **NULLABLE)
    category = models.ForeignKey('catalog.Category', on_delete=models.PROTECT)
    price = models.PositiveIntegerField()
    date_of_born = models.DateTimeField(auto_now_add=True, **NULLABLE)
    date_of_change = models.DateTimeField(auto_now=True, **NULLABLE)

    def __str__(self):
        return f'{self.title}'
    class Meta:
        verbose_name = 'продкут'
        verbose_name_plural = 'продукты'


class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    description = models.TextField(**NULLABLE)

    def __str__(self):
        return f'{self.title}'
