# Generated by Django 2.2 on 2020-09-11 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0003_book_old_test_2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='Old_Test_2',
        ),
        migrations.AlterField(
            model_name='book',
            name='Old_Test',
            field=models.BooleanField(default=False),
        ),
    ]