from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    avatar = models.ImageField(upload_to='catalog/', null=True, blank=True)
    category = models.ForeignKey('catalog.Category', on_delete=models.PROTECT)
    price = models.IntegerField()
    date_of_born = models.DateTimeField(auto_now_add=True, null=True)
    date_of_change = models.DateTimeField(auto_now=True ,null=True)

    def __str__(self):
        return f'{self.title}, {self.category}, {self.price}'
    class Meta:
        verbose_name = 'продкут'
        verbose_name_plural = 'продукты'


class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    discription = models.TextField()

    def __str__(self):
        return f'{self.title}, {self.discription}'
