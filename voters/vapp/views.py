from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Goverment, Politikai
from .serializers import UserRegisterationSerializer, PolitikaiSerializer, GovermentSerializer
from rest_framework.decorators import api_view, permission_classes, APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status


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
    if not politikai_id:
        return Response({"error": "Missing politikai_id"}, status=status.HTTP_400_BAD_REQUEST)
    try:
        politikai = Politikai.objects.get(id=politikai_id)
    except Politikai.DoesNotExist:
        return Response({"error": "Politikai not found"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    data = {
        "first_name": politikai.first_name,
        "last_name": politikai.last_name,
    }
    if politikai.profile_picture and hasattr(politikai.profile_picture, 'url'):
        data['profile_picture'] = politikai.profile_picture.url
    return Response(data)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def show_profiles(request):
    custom_party = request.data
    if not isinstance(custom_party, dict) or not custom_party:
        return Response({"error": "Invalid or missing custom party"})
    profiles_ids = list(custom_party.values())
    print(profiles_ids)
    profiles = Politikai.objects.filter(id__in=profiles_ids)
    profiles_data = {}
    for profile in profiles:
        profiles_data[profile.id] = {
            "first_name": profile.first_name,
            "last_name": profile.last_name,
            "profile_picture": profile.profile_picture.url if profile.profile_picture and hasattr(profile.profile_picture, "url") else None
        }
    return Response({"ok": profiles_data})
