# Generated by Django 4.2.4 on 2023-08-26 16:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("shop", "0009_alter_pricechoices_lower_limit_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Consultation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "user_custom_name",
                    models.CharField(
                        blank=True, max_length=50, verbose_name="Имя в заявке"
                    ),
                ),
                (
                    "date_created",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата и время регистрации"
                    ),
                ),
                ("done", models.BooleanField(default=False, verbose_name="Отработана")),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь",
                    ),
                ),
            ],
            options={
                "verbose_name": "Заявка на консультацию",
                "verbose_name_plural": "Заявки на консультацию",
            },
        ),
    ]
