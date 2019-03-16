
from django.urls import path
from .views import (
    Options_list_view, 
    Options_detail_view, 
    Options_create_view, 
    Options_delete_view,
    Options_edit_view,
)

urlpatterns = [
    path('', Options_list_view.as_view(), name='Options-list'),
    path('detail/<pk>', Options_detail_view.as_view(), name='Options-detail'),
    path('create/<pk>', Options_create_view.as_view(), name='Options-create'),
    path('delete/<pk>', Options_delete_view.as_view(),name='Options-delete'),
    path('edit/<pk>/<no>', Options_edit_view.as_view(),name='Options-edit'),
]

