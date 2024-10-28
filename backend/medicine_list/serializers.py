from rest_framework import serializers
from medicine_list.models import MedicineList,Manufacturer

class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = '__all__'


class MedicineListSerializer(serializers.ModelSerializer):
    manufacturer = ManufacturerSerializer() 
    class Meta:
        model = MedicineList
        fields = '__all__'

