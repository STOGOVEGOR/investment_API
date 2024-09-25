from django.contrib import admin
from django.urls import path

from .views import ClientCreateView, InvestCreateView

urlpatterns = [
    path('clients/', ClientCreateView.as_view(), name='clients'),
    path('invest/<int:client_id>/', InvestCreateView.as_view(), name='clients'),
]
