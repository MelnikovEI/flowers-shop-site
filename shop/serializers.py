from rest_framework.serializers import ModelSerializer
from shop.models import Product, Situation, PriceChoices


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
