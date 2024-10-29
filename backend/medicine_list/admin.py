from django.contrib import admin
from medicine_list.models import Manufacturer, MedicineList

class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

class MedicineListAdmin(admin.ModelAdmin):
    list_display = ('name', 'generic_name', 'manufacturer', 'price','created_at', 'updated_at')
    list_filter = ('manufacturer',)
    search_fields = ('name', 'generic_name')


admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(MedicineList, MedicineListAdmin)