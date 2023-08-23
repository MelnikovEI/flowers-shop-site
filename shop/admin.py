from django.contrib import admin

from shop.models import Order, Situation, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


# class ProductInline(admin.TabularInline):
#     model = Product


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass
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


@admin.register(Situation)
class SituationAdmin(admin.ModelAdmin):
    pass


