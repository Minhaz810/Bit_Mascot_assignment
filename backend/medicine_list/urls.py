from django.urls import path
from medicine_list.views import MedicineListAdminApiView,MedicineListPublicApiView,ManufacturerListAPIView

urlpatterns = [
    path('public/medicine_list',MedicineListPublicApiView.as_view(),name='test_view'),
    path('public/manufacturer_list',ManufacturerListAPIView.as_view(),name='test_view'),
    path('admin/medicine_list',MedicineListAdminApiView.as_view(),name='test_view')
]
