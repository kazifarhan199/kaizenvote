from django.urls import path
from .views import (
    Voots_list_view, 
    Voots_detail_view, 
)

urlpatterns = [
    path('', Voots_list_view.as_view(), name='Voots-list'),
    path('detail/<pk>', Voots_detail_view.as_view(), name='Voots-detail'),
]

