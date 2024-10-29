from rest_framework import serializers
from medicine_list.models import MedicineList,Manufacturer

class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ['id', 'name', 'description']


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
    
    def update(self, instance, validated_data):
        manufacturer_data = validated_data.pop('manufacturer', None)
        
        if manufacturer_data:
            manufacturer_id = manufacturer_data.get("id")
            if manufacturer_id:
                manufacturer_instance = Manufacturer.objects.get(id=manufacturer_id)
                for attr, value in manufacturer_data.items():
                    setattr(manufacturer_instance, attr, value)
                manufacturer_instance.save()
                instance.manufacturer = manufacturer_instance
            else:
                instance.manufacturer = Manufacturer.objects.create(**manufacturer_data)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        instance.save()
        return instance
