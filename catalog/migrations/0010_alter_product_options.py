# Generated by Django 4.2.2 on 2023-08-14 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_alter_product_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'продкут', 'verbose_name_plural': 'продукты'},
        ),
    ]
