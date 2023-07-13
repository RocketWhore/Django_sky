

from django.db import migrations, models
#fmdm

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('discription', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('avatar', models.ImageField(upload_to='catalog/')),
                ('category', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('date_of_born', models.DateTimeField()),
                ('date_of_change', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'продкут',
                'verbose_name_plural': 'продукты',
            },
        ),
    ]