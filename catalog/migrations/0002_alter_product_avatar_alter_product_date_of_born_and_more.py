# Generated by Django 4.2.2 on 2023-07-17 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='catalog/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='date_of_born',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='date_of_change',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
