from django.urls import path
from .views import TreePageView, ListPageView

urlpatterns = [
    path('', TreePageView.as_view(), name='tree'),
    path('tree', TreePageView.as_view(), name='tree'),
    path('list', ListPageView.as_view(), name='list'),
]