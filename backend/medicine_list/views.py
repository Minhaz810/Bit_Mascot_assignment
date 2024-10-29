from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework import status

from medicine_list.models import MedicineList, Manufacturer
from medicine_list.serializers import MedicineListSerializer,ManufacturerSerializer
from django.db.models import Q
from django.shortcuts import get_object_or_404


class MedicineListPublicApiView(APIView):
    def get(self,request):
        query = request.query_params.get('query',None)
        medicine_list = MedicineList.objects.all().order_by('-updated_at')

        if query:
            medicine_list = medicine_list.filter(
                    Q(name__icontains=query) | 
                    Q(batch_number__icontains=query) |
                    Q(generic_name__icontains=query)
                ).order_by('-updated_at')
        
        paginator = PageNumberPagination()
        paginator.page_size = 3
        paginated_queryset = paginator.paginate_queryset(medicine_list, request)

        serializer  = MedicineListSerializer(paginated_queryset,many=True)
        data        = serializer.data

        return paginator.get_paginated_response(data)
    

class MedicineListAdminApiView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        query = request.query_params.get('query',None)
        medicine_list = MedicineList.objects.all().order_by('-updated_at')

        if query:
            medicine_list = medicine_list.filter(
                    Q(name__icontains=query) | 
                    Q(batch_number__icontains=query) |
                    Q(generic_name__icontains=query)
                ).order_by('-updated_at')
        
        paginator = PageNumberPagination()
        paginator.page_size = 10
        paginated_queryset = paginator.paginate_queryset(medicine_list, request)

        serializer  = MedicineListSerializer(paginated_queryset,many=True)
        data        = serializer.data

        return paginator.get_paginated_response(data)
    
    def post(self, request):
        data = request.data
        serializer = MedicineListSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request):
        medicine_id = request.data.get("id")
        manufacturer_id = request.data.get("manufacturer").get("id")
        name = request.data.get("name")
        generic_name = request.data.get("generic_name")
        description = request.data.get("description")
        price = request.data.get("price")
        batch_number = request.data.get("batch_number")
        other_related_details = request.data.get("other_related_detailes")

        if not medicine_id:
            return Response({"error": "Medicine ID required"}, status=status.HTTP_400_BAD_REQUEST)
        if not manufacturer_id:
            return Response({"error": "Manufacturer ID required"}, status=status.HTTP_400_BAD_REQUEST)

        medicine_list_item = get_object_or_404(MedicineList, id=medicine_id)
        manufacturer = get_object_or_404(Manufacturer,id=manufacturer_id)
        
        
        medicine_list_item.name = name
        medicine_list_item.generic_name = generic_name
        medicine_list_item.description = description
        medicine_list_item.price = price
        medicine_list_item.batch_number = batch_number
        medicine_list_item.other_related_details = other_related_details
        medicine_list_item.manufacturer = manufacturer

        medicine_list_item.save()
        return Response(
            {
                "message": f"Successfully updated medicine with id-{medicine_id}"
            }, 
            status=status.HTTP_200_OK
        )
    
    def delete(self, request):
        medicine_id = request.query_params.get("id")
        
        if not medicine_id:
            return Response({"error": "ID required"}, status=status.HTTP_400_BAD_REQUEST)
        
        medicine_list_item = get_object_or_404(MedicineList, id=medicine_id)
        medicine_list_item.delete()
        return Response(
                    {
                        "message":f"successfully deleted medicine with id-{medicine_id}"
                    }, 
                    status=status.HTTP_200_OK
                )


class ManufacturerListAPIView(APIView):
    def get(self,request):
        manufacturer_list = Manufacturer.objects.all()
        serializer  = ManufacturerSerializer(manufacturer_list,many=True)
        data        = serializer.data

        return Response({
            "results":data
        },status=status.HTTP_200_OK)


