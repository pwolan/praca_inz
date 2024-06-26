from django.shortcuts import render
from django.http import HttpRequest
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from .models import *
# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def send_some_data(request: HttpRequest):
   
    return Response({
        "data": "Hello from parent api",
    })

