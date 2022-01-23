from django.urls import path
from .views import OrderList, OrderDetail


urlpatterns = [
    path('order', OrderList.as_view(), name='orders'),
    path('order/<str:label>', OrderDetail.as_view(), name='order-update'),
]
