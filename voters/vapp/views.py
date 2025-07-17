from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Goverment, Politikai
from .serializers import UserRegisterationSerializer, PolitikaiSerializer, GovermentSerializer, UserSerializer
from rest_framework.decorators import api_view, permission_classes, APIView
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
    

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def add_politikai(request):
    user = request.user
    if user.is_superuser:
        data = request.data
        serializer = PolitikaiSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"validation success": True})
        return Response({"validation success": False})
    return Response({"Error": "User does not have premission."})


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def add_goverment(request):
    user = request.user
    data = request.data
    data["user"] = user.id
    serializer = GovermentSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({"goverment": serializer.data})
    return Response({"validation success": False, "error": serializer.errors})


class PolitikaiBulkUploadView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        if not isinstance(data, list):
            return Response({"error": "Expected a list of items"})
        
        serializer = PolitikaiSerializer(data=data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": f"{len(serializer.data)} Politikai created successfully"})
        else:
            return Response(serializer.errors)
        
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def show_goverment(request):
    user = request.user
    goverment = Goverment.objects.get(user=user.id)
    serializer = GovermentSerializer(goverment)
    return Response(serializer.data)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def show_politikai(request):
    politikai_id = request.GET.get('politikai_id') 
    politikai = Politikai.objects.get(id=politikai_id)
    serializer = PolitikaiSerializer(politikai)
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def show_profile(request):
    politikai_id = request.GET.get('politikai_id')
    politikai = Politikai.objects.get(id=politikai_id)
    data = {
        "first_name": politikai.first_name,
        "last_name": politikai.last_name,
    }
    if politikai.profile_picture is not None:
        data['profile_picture'] = politikai.profile_picture.url
    return Response(data)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def show_user_data(request):
    user = request.user
    serializer = UserSerializer(user)
    return Response(serializer.data)
