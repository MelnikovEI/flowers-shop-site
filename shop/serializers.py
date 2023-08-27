from django.db import transaction
from django.shortcuts import get_object_or_404
from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework.fields import CharField, IntegerField, ChoiceField
from rest_framework.serializers import ModelSerializer, Serializer
from shop.models import Product, Situation, PriceChoices, Order, ShopUser, UserRole
from django.contrib.auth.models import User


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class SituationSerializer(ModelSerializer):
    class Meta:
        model = Situation
        fields = '__all__'


class PriceChoicesSerializer(ModelSerializer):
    class Meta:
        model = PriceChoices
        fields = '__all__'


class OrderSerializer(Serializer):
    client_name = CharField(max_length=100)
    phone_number = PhoneNumberField(region='RU')
    address = CharField(max_length=100)
    delivery_time_range = ChoiceField(
        required=False,
        choices=Order.DeliveryTimeRange.choices,
        default=Order.DeliveryTimeRange.AS_POSSIBLE,
    )

    @transaction.atomic
    def create(self, validated_data):
        user, created = User.objects.get_or_create(
            username=str(validated_data['phone_number']),
            defaults={
                'first_name': validated_data['client_name'],
                'password': User.objects.make_random_password(),
            }
        )
        if not created:
            user.first_name = validated_data['client_name']
            user.save(update_fields=['first_name'])
        shop_user, created = ShopUser.objects.get_or_create(
            user=user,
            defaults={
                'phone_number': validated_data['phone_number'],
            }
        )
        shop_user.roles.add(get_object_or_404(UserRole, role=1))
        product = get_object_or_404(Product, pk=validated_data['product_id'])
        order = Order.objects.create(
            client=shop_user,
            address=validated_data['address'],
            delivery_time_range=validated_data['delivery_time_range']
        )
        order.product.add(product)
        return order
    """
    def update(self, instance, validated_data):
        '''Update and return an existing `Snippet` instance, given the validated data.'''
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance
    """
