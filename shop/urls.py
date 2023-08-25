from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from shop import views


urlpatterns = [
    path('', views.index, name='index'),
    path('card/<int:product_id>', views.card, name='card'),
    path('catalog/', views.catalog, name='catalog'),
    path('consultation/', views.consultation, name='consultation'),
    path('order/<int:product_id>', views.order, name='order'),
    path('order-step/', views.order_step, name='order_step'),
    path('quiz/', views.quiz, name='quiz'),
    path('quiz-step/<int:situation_id>', views.quiz_step, name='quiz_step'),
    path('result/<int:product_id>', views.result, name='result'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
