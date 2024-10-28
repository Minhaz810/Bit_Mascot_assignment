from django.db import models


class Manufacturer(models.Model):
    name         = models.CharField(max_length=255,null=True,blank=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class MedicineList(models.Model):
    name                    = models.CharField(max_length=255,null=True,blank=True)
    generic_name            = models.CharField(max_length=255,null=True,blank=True)
    manufacturer            = models.ForeignKey(Manufacturer, on_delete = models.CASCADE, null= True, blank= True, related_name= 'manufacturer')
    description             = models.TextField()
    price                   = models.DecimalField(max_digits=5, decimal_places=2)
    batch_number            = models.BigIntegerField(null= True, blank= True, default = 0)
    other_related_detailes  = models.TextField()

    def __str__(self):
        return self.name
