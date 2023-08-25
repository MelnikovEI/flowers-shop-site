from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from phonenumber_field.modelfields import PhoneNumberField


class UserRole(models.Model):
    class Roles(models.IntegerChoices):
        CLIENT = 1, 'Клиент'
        COURIER = 2, 'Курьер'
        FLORIST = 3, 'Флорист'

    role = models.IntegerField(
        choices=Roles.choices,
        unique=True,
        default=Roles.CLIENT
    )

    class Meta:
        verbose_name = 'Роль пользователя'
        verbose_name_plural = 'Роли пользователей'

    def __str__(self):
        return self.get_role_display()


class ShopUser(models.Model):
    user = models.OneToOneField(User, related_name='shop_user', on_delete=models.CASCADE)
    phone_number = PhoneNumberField('Номер телефона', region='RU')
    roles = models.ManyToManyField(UserRole, verbose_name='Роли', related_name='shop_users')

    class Meta:
        verbose_name = 'Пользователь магазина'
        verbose_name_plural = 'Пользователи магазина'

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


class Situation(models.Model):
    name = models.CharField(
        'ситуация',
        unique=True,
        max_length=50
    )

    class Meta:
        verbose_name = 'ситуация'
        verbose_name_plural = 'ситуации'

    def __str__(self):
        return self.name


class ProductQuerySet(models.QuerySet):
    def filtered(self, situation_id, price_limit_id):
        price_limit = get_object_or_404(PriceChoices, pk=price_limit_id)
        min_price = price_limit.lower_limit
        max_price = price_limit.upper_limit
        filtered_products = self.filter(situation__pk=situation_id, price__gte=min_price, price__lte=max_price)
        return filtered_products


class Product(models.Model):
    situation = models.ManyToManyField(
        Situation,
        related_name='situations',
        verbose_name='ситуация',
    )
    title = models.CharField(
        'название',
        unique=True,
        max_length=50
    )
    price = models.DecimalField(
        'цена в каталоге',
        max_digits=6,
        decimal_places=0,
        validators=[MinValueValidator(0)]
    )
    image = models.ImageField(
        'картинка'
    )
    description = models.TextField(
        'описание',
        max_length=1000,
        blank=True,
    )

    objects = ProductQuerySet.as_manager()

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'

    def __str__(self):
        return self.title


class Order(models.Model):
    class Statuses(models.IntegerChoices):
        PENDING = 1, 'Обработать'
        ASSEMBLY = 2, 'Собрать'
        DELIVER = 3, 'Доставить'
        FINISHED = 4, 'Выполнен'
    status = models.IntegerField(
        choices=Statuses.choices,
        default=Statuses.PENDING,
    )
    product = models.ManyToManyField(
        Product,
        related_name='orders',
        verbose_name='продукт',
    )
    client = models.ForeignKey(
        ShopUser,
        on_delete=models.PROTECT,
        related_name='client_orders',
        verbose_name='клиент',
        limit_choices_to={'roles__role':UserRole.Roles.CLIENT}
    )
    courier = models.ForeignKey(
        ShopUser,
        on_delete=models.SET_NULL,
        verbose_name='курьер',
        related_name='courier_orders',
        limit_choices_to={'roles__role': UserRole.Roles.COURIER},
        blank=True, null=True
    )
    florist = models.ForeignKey(
        ShopUser,
        on_delete=models.SET_NULL,
        verbose_name='флорист',
        related_name='florist_orders',
        limit_choices_to={'roles__role': UserRole.Roles.FLORIST},
        blank=True, null=True
    )
    address = models.CharField('Адрес доставки', max_length=100)
    comment = models.TextField('Комментарий', max_length=500, blank=True)
    created_at = models.DateTimeField('Заказ создан', auto_now_add=True)
    called_at = models.DateTimeField('Звонок совершён', null=True, blank=True)
    assembled_at = models.DateTimeField('Собран', null=True, blank=True)
    delivered_at = models.DateTimeField('Доставлен', null=True, blank=True)

    # objects = OrderQuerySet.as_manager()

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        indexes = [
            models.Index(fields=['status', 'created_at', 'called_at', 'delivered_at', ]),
        ]

    def __str__(self):
        return f"{self.client} {self.address}"


class PriceChoices(models.Model):
    title = models.CharField(
        'Название',
        unique=True,
        max_length=50
    )
    lower_limit = models.PositiveSmallIntegerField('Минимальная цена')
    upper_limit = models.PositiveSmallIntegerField('Максимальная цена')

    class Meta:
        verbose_name = 'Фильтр цен'
        verbose_name_plural = 'Фильтры цен'

    def __str__(self):
        return self.title
