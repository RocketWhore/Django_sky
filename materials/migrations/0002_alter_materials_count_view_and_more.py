# Generated by Django 4.2.2 on 2023-07-28 20:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materials',
            name='count_view',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='materials',
            name='date_of_create',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='materials',
            name='preview',
            field=models.ImageField(blank=True, null=True, upload_to='materials_image'),
        ),
        migrations.AlterField(
            model_name='materials',
            name='sign_of_pub',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
