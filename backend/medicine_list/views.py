from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework import status

from medicine_list.models import MedicineList, Manufacturer
from medicine_list.serializers import MedicineListSerializer
from django.db.models import Q


class MedicineListPublicApiView(APIView):
    def get(self,request):
        query = request.query_params.get('query',None)
        medicine_list = MedicineList.objects.all()

        if query:
            medicine_list = medicine_list.filter(
                    Q(name__icontains=query) | 
                    Q(batch_number__icontains=query) |
                    Q(generic_name__icontains=query)
                )
        
        paginator = PageNumberPagination()
        paginator.page_size = 10
        paginated_queryset = paginator.paginate_queryset(medicine_list, request)

        serializer  = MedicineListSerializer(paginated_queryset,many=True)
        data        = serializer.data

        return paginator.get_paginated_response(data)
    
    
class MedicineListAdminApiView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        query = request.query_params.get('query',None)
        medicine_list = MedicineList.objects.all()

        if query:
            medicine_list = medicine_list.filter(
                    Q(name__icontains=query) | 
                    Q(batch_number__icontains=query) |
                    Q(generic_name__icontains=query)
                )
        
        paginator = PageNumberPagination()
        paginator.page_size = 10
        paginated_queryset = paginator.paginate_queryset(medicine_list, request)

        serializer  = MedicineListSerializer(paginated_queryset,many=True)
        data        = serializer.data

        return paginator.get_paginated_response(data)