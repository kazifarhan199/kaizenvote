
from django.urls import path
from .views import (
    Title_list_view, 
    Title_detail_view, 
    Title_create_view, 
    Title_delete_view,
    Title_edit_view,
)

urlpatterns = [
    path('', Title_list_view.as_view(), name='Title-list'),
    path('detail/<pk>', Title_detail_view.as_view(), name='Title-detail'),
    path('create/', Title_create_view.as_view(), name='Title-create'),
    path('delete/<pk>', Title_delete_view.as_view(),name='Title-delete'),
    path('edit/<pk>', Title_edit_view.as_view(),name='Title-edit'),
]

