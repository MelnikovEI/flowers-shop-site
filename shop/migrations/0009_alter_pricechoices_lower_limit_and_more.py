# Generated by Django 4.2.4 on 2023-08-25 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_pricechoices_alter_order_client_alter_order_courier_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricechoices',
            name='lower_limit',
            field=models.PositiveIntegerField(verbose_name='Минимальная цена'),
        ),
        migrations.AlterField(
            model_name='pricechoices',
            name='upper_limit',
            field=models.PositiveIntegerField(verbose_name='Максимальная цена'),
        ),
    ]
