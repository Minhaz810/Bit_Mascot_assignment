from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status


class MedicineListAdminApiView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        return Response({
            "message":"This is a test response"
        },status= status.HTTP_200_OK)
    
class MedicineListPublicApiView(APIView):
    def get(self,request):
        return Response({
            "message":"This is a test response"
        },status= status.HTTP_200_OK)