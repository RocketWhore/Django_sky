# Generated by Django 4.2.2 on 2023-07-28 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_rename_discription_category_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='название')),
                ('slug', models.CharField(max_length=150, verbose_name='slug')),
                ('body', models.TextField()),
                ('preview', models.ImageField(blank=True, null=True, upload_to='catalog/')),
                ('date_of_create', models.DateTimeField(auto_now_add=True, null=True)),
                ('sign_of_pub', models.BooleanField(blank=True, null=True)),
                ('count_view', models.PositiveIntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'материал',
                'verbose_name_plural': 'материалы',
            },
        ),
    ]
