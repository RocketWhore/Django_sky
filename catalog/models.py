from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    avatar = models.ImageField(upload_to='catalog/')
    category = models.CharField(max_length=100)
    price = models.IntegerField()
    date_of_born = models.DateTimeField()
    date_of_change = models.DateTimeField()

    def __str__(self):
        return f'{self.title}, {self.category}, {self.price}'
    class Meta:
        verbose_name = 'продкут'
        verbose_name_plural = 'продукты'


class Category(models.Model):
    title = models.CharField(max_length=100)
    discription = models.TextField()

    def __str__(self):
        return f'{self.title}, {self.discription}'
