from django.shortcuts import render, get_object_or_404
from shop.models import Product, Situation, PriceChoices
from shop.serializers import ProductSerializer, SituationSerializer, PriceChoicesSerializer


def index(request):
    return render(request, template_name='index.html', context={})


def card(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    serializer = ProductSerializer(product)
    return render(request, template_name='card.html', context={'product': serializer.data})


def catalog(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return render(request, template_name='catalog.html', context={'products': serializer.data})


def order_step(request):
    return render(request, template_name='order-step.html', context={})


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


def result(request, situation_id, price_limit_id,):
    # TODO: выбрать букет, соответствующий заданным критериям
    product = get_object_or_404(Product, pk=1)
    serializer = ProductSerializer(product)
    return render(request, template_name='result.html', context={'product': serializer.data})


def consultation(request):
    return render(request, template_name='consultation.html', context={})


def order(request, product_id):
    return render(request, template_name='order.html', context={})
