# Generated by Django 3.2.20 on 2023-07-11 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='spices',
            options={'verbose_name_plural': 'Spices'},
        ),
    ]
