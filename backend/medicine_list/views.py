from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework import status

from medicine_list.models import MedicineList, Manufacturer
from medicine_list.serializers import MedicineListSerializer
from django.db.models import Q
from django.shortcuts import get_object_or_404


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
        paginator.page_size = 3
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
    
    def post(self, request):
        data = request.data
        serializer = MedicineListSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request):
        medicine_id = request.data.get("id")
        if not medicine_id:
            return Response({"error": "ID required"}, status=status.HTTP_400_BAD_REQUEST)

        medicine_list_item = get_object_or_404(MedicineList, id=medicine_id)
        serializer = MedicineListSerializer(medicine_list_item, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(
                    {
                        "message":f"successfully updated medicine with id-{medicine_id}"
                    }, 
                    status=status.HTTP_200_OK
                )
    
    def delete(self, request):
        medicine_id = request.data.get("id")
        
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
