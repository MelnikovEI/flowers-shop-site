from django.shortcuts import render


def index(request):
    return render(request, template_name='index.html', context={})


def card(request):
    return render(request, template_name='card.html', context={})


def catalog(request):
    return render(request, template_name='catalog.html', context={})


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


