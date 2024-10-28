from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework import status

from medicine_list.models import MedicineList, Manufacturer
from medicine_list.serializers import MedicineListSerializer


class MedicineListAdminApiView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        return Response({
            "message":"This is a test response"
        },status= status.HTTP_200_OK)
    
class MedicineListPublicApiView(APIView):
    def get(self,request):
        paginator = PageNumberPagination()
        paginator.page_size = 10
        medicine_list = MedicineList.objects.all()
        paginated_queryset = paginator.paginate_queryset(medicine_list, request)

        serializer  = MedicineListSerializer(paginated_queryset,many=True)
        data        = serializer.data

        return paginator.get_paginated_response(data)