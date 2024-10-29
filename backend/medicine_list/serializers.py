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

    def create(self, validated_data):
        manufacturer_data = validated_data.pop('manufacturer')
        manufacturer, created = Manufacturer.objects.get_or_create(**manufacturer_data)
        medicine_list = MedicineList.objects.create(manufacturer=manufacturer, **validated_data)
        return medicine_list