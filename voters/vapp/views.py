from django.shortcuts import render
from django.contrib.auth.models import User

from .serializers import UserRegisterationSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny



@api_view(["POST"])
def logout(request):
    try:
        res = Response()
        res.data = {"success": True}
        res.delete_cookie('access_token', path='/', samesite='None')
        res.delete_cookie('refresh_token', path='/', samesite='None')

        return res
    except:
        return Response({"success": False})
    
@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    serializer = UserRegisterationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)