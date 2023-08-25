
from django.urls import path
from interview.order.views import OrderListCreateView, OrderTagListCreateView, OrdersByTagListView


urlpatterns = [
    path('tags/', OrderTagListCreateView.as_view(), name='order-detail'),
    path('tags/<str:tag_name>/', OrdersByTagListView.as_view(), name='orders-by-tag'),
    path('', OrderListCreateView.as_view(), name='order-list'),

]