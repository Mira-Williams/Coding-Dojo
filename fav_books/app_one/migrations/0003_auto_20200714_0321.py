# Generated by Django 2.2 on 2020-07-14 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_one', '0002_auto_20200713_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='favorited_by',
            field=models.ManyToManyField(related_name='favorite_books', to='app_one.User'),
        ),
    ]
