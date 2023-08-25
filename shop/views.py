from django.shortcuts import render
from shop.models import Product
from shop.serializers import ProductSerializer


def index(request):
    return render(request, template_name='index.html', context={})


def card(request):
    return render(request, template_name='card.html', context={})


def catalog(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return render(request, template_name='catalog.html', context={'products': serializer.data})


def consultation(request):
    return render(request, template_name='consultation.html', context={})


def order(request):
    return render(request, template_name='order.html', context={})


def order_step(request):
    return render(request, template_name='order-step.html', context={})


def quiz(request):
    return render(request, template_name='quiz.html', context={})


def quiz_step(request):
    return render(request, template_name='quiz-step.html', context={})


def result(request):
    return render(request, template_name='result.html', context={})


