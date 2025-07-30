from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.response import Response

class UserokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        token['username'] = user.username
        token['email'] = user.email
        return token

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = UserokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        try:
            response = super().post(request, *args, **kwargs)
            tokens = response.data

            res = Response()
            res.data = {"success": True}
            res.set_cookie("access_token", tokens["access"], httponly=True, secure=False, samesite="Lax", path="/")
            res.set_cookie("refresh_token", tokens["refresh"], httponly=True, secure=False, samesite="Lax", path="/")
            return res
        except:
            print(super().post(request=request, *args, **kwargs))
            return Response({"success": False})

class CustomRefreshTokenView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.COOKIES.get('refresh_token')

            if not refresh_token:
                return Response({"Error": "No refresh token provided"})
        
            request.data['refresh'] = refresh_token
            
            response = super().post(request, *args, **kwargs)
            res = Response()
            res.data = {"Refreshed": True}
            res.set_cookie("access_token", response.data["access"], httponly=True, secure=False, samesite="Lax", path="/")
            res.set_cookie("refresh_token", response.data["refresh"], httponly=True, secure=False, samesite="Lax", path="/")
            return res
        except:
            return Response({"Refreshed": False})



