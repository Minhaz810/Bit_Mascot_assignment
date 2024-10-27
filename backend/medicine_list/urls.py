from django.urls import path
from medicine_list.views import TestView

urlpatterns = [
    path('test',TestView.as_view(),name='test_view')
]
