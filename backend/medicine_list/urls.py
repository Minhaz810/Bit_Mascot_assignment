from django.urls import path
from medicine_list.views import MedicineListAdminApiView,MedicineListPublicApiView

urlpatterns = [
    path('public/medicine_list',MedicineListPublicApiView.as_view(),name='test_view'),
    path('admin/medicine_list',MedicineListAdminApiView.as_view(),name='test_view')
]
