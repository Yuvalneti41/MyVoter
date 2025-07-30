from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView
)
from .custom_jwt_views import CustomTokenObtainPairView, CustomRefreshTokenView
from .views import logout, register, add_politikai, add_goverment, show_goverment, show_politikai, show_profile, show_profiles, PolitikaiBulkUploadView

urlpatterns = [
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', CustomRefreshTokenView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/logout/', logout, name='logout'),
    path('api/register/', register, name='register'),
    path('api/add_politikai/', add_politikai, name='add_politikai'),
    path('politikai/bulk-upload/', PolitikaiBulkUploadView.as_view(), name='politikai-bulk-upload'),
    path('api/add_goverment/', add_goverment, name='add_goverment'),
    path('api/goverment/', show_goverment, name='show_goverment'),
    path('api/politikai/', show_politikai, name='show_politikai'),
    path('api/politikai/profile/', show_profile, name='show_profile'),
    path('api/politikai/profiles/', show_profiles, name="show_profiles")
]