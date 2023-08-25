# Generated by Django 4.2.4 on 2023-08-23 16:51

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Courier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Florist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(1, 'Обработать'), (2, 'Собрать'), (3, 'Доставить'), (4, 'Выполнен')], default=1)),
                ('address', models.CharField(max_length=100, verbose_name='Адрес доставки')),
                ('comment', models.TextField(blank=True, max_length=500, verbose_name='Комментарий')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Заказ создан')),
                ('called_at', models.DateTimeField(blank=True, null=True, verbose_name='Звонок совершён')),
                ('delivered_at', models.DateTimeField(blank=True, null=True, verbose_name='Доставлен')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='orders', to='shop.client', verbose_name='клиент')),
                ('courier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='shop.courier', verbose_name='курьер')),
                ('florist', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='shop.florist', verbose_name='флорист')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.CreateModel(
            name='Situation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='ситуация')),
            ],
            options={
                'verbose_name': 'ситуация',
                'verbose_name_plural': 'ситуации',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True, verbose_name='название')),
                ('price', models.DecimalField(decimal_places=0, max_digits=6, validators=[django.core.validators.MinValueValidator(0)], verbose_name='цена в каталоге')),
                ('image', models.ImageField(upload_to='', verbose_name='картинка')),
                ('description', models.TextField(blank=True, max_length=200, verbose_name='описание')),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='shop.order', verbose_name='продукт')),
                ('situation', models.ManyToManyField(related_name='situations', to='shop.situation', verbose_name='ситуация')),
            ],
            options={
                'verbose_name': 'товар',
                'verbose_name_plural': 'товары',
            },
        ),
        migrations.AddIndex(
            model_name='order',
            index=models.Index(fields=['status', 'created_at', 'called_at', 'delivered_at'], name='shop_order_status_1fbdce_idx'),
        ),
        migrations.RemoveField(
            model_name='product',
            name='order',
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ManyToManyField(related_name='orders', to='shop.product', verbose_name='продукт'),
        ),
        migrations.AddField(
            model_name='order',
            name='assembled_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Собран'),
        ),
    ]