from django.urls import path
from .views import *

urlpatterns = [
    path('notice-list', NoticeListView.as_view(), name='notice-list'),
    path('notice/<int:pk>/', NoticeView.as_view(), name='notice')
]