# Generated by Django 2.2 on 2020-09-11 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0006_book_num_verses'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Book', models.CharField(max_length=255)),
                ('Number', models.IntegerField(null=True)),
                ('num_verses', models.IntegerField(null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
        ),
    ]
