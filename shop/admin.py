from django.contrib import admin
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from shop.models import Order, Situation, Product, ShopUser, UserRole, PriceChoices, Consultation


class OrderInline(admin.TabularInline):
    model = Order


class ShopUserInline(admin.StackedInline):
    model = ShopUser
    verbose_name = 'Данные пользователя магазина'


class UserAdmin(BaseUserAdmin):
    inlines = [ShopUserInline]
    list_display = ['username','get_fist_last_name', 'get_roles']
    list_display_links = ['username']

    @admin.display(description='ФИО пользователя')
    def get_fist_last_name(self, instance):
        return f'{instance.first_name} {instance.last_name}'

    @admin.display(description='Роль')
    def get_roles(self, instance: User):
        return list(instance.shop_user.roles.all())


admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# class ProductInline(admin.TabularInline):
#     model = Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ["preview"]

    def preview(self, instance):
        return mark_safe(f'<img src="{instance.image.url}" style="max-height: 200px;">')


@admin.register(Situation)
class SituationAdmin(admin.ModelAdmin):
    pass


@admin.register(PriceChoices)
class PriceChoicesAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ['delivery_time_range', 'created_at']
    list_filter = ['status', 'delivery_time_range', 'florist', 'courier']
    # readonly_fields = ['created_at', ]
    # fields = (
    #     'address',
    #     'created_at',
    #     ('called_at', 'delivered_at'),
    #     ('status'),
    # )
    # list_display = [
    #     'address',
    # ]
    # inlines = [
    #     ProductInline,
    # ]


@admin.register(UserRole)
class UserRoleAdmin(admin.ModelAdmin):
    pass


@admin.register(Consultation)
class ConsultationAdmin(admin.ModelAdmin):
    readonly_fields = ['user', 'date_created']
    list_filter = [
        'done',
    ]
