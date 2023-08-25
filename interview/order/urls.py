
from django.urls import path
from interview.order.views import OrderListCreateView, OrderTagListCreateView, OrderTagListView


urlpatterns = [
    path('tags/', OrderTagListCreateView.as_view(), name='order-detail'),
    path('<int:pk>/tags/', OrderTagListView.as_view(), name='order-tags'),
    path('', OrderListCreateView.as_view(), name='order-list'),

]