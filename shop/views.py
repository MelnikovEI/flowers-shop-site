import random
from django.db import transaction
from django.shortcuts import render, get_object_or_404
from django.template.defaultfilters import random
from rest_framework.decorators import api_view

from shop.models import Product, Situation, PriceChoices, Order
from shop.serializers import ProductSerializer, SituationSerializer, PriceChoicesSerializer, OrderSerializer, \
    ConsultationSerializer


def index(request, alert: str = None):
    random_products_ids = Product.objects.all().order_by('?')[:3].values_list('id', flat=True)
    random_products = Product.objects.filter(id__in=random_products_ids)
    if not alert:
        return render(request, template_name='index.html', context={'products_for_main': random_products})
    else:
        return render(request, template_name='index.html',
                      context={'products_for_main': random_products, 'alert': alert})


def card(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    serializer = ProductSerializer(product)
    return render(request, template_name='card.html', context={'product': serializer.data})


def catalog(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return render(request, template_name='catalog.html', context={'products': serializer.data})


def quiz(request):
    situations = Situation.objects.all()
    serializer = SituationSerializer(situations, many=True)
    return render(request, template_name='quiz.html', context={'situations': serializer.data})


def quiz_step(request, situation_id):
    price_choices = PriceChoices.objects.all()
    serializer = PriceChoicesSerializer(price_choices, many=True)
    return render(
        request,
        template_name='quiz-step.html',
        context={
            'situation_id': situation_id,
            'price_choices': serializer.data
        }
    )


def result(request, situation_id, price_limit_id):
    products = Product.objects.filtered(situation_id, price_limit_id)
    serializer = ProductSerializer(products, many=True)
    return render(request, template_name='result.html', context={'products': serializer.data})


@transaction.atomic
@api_view(['POST'])
def consultation(request):
    serializer = ConsultationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return render(request, template_name='consultation.html', context={})


def order(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    serializer = ProductSerializer(product)
    return render(
        request, template_name='order.html',
        context={'product': serializer.data, 'delivery_ranges': Order.DeliveryTimeRange.choices}
    )


@transaction.atomic
@api_view(['POST'])
def order_step(request, product_id):
    stage = request.POST.get('stage')
    if stage == 'payment':
        return index(request, 'Ваш заказ оплачен. С вами свяжутся в ближайшее время для подтверждения доставки')
    serializer = OrderSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save(product_id=product_id)
    return render(request, template_name='order-step.html', context={'product_id':product_id})


def stats(request):
    return render(request, template_name='stats.html', context={})