
from .views import UserRegistration, UserLogin
# from knox import views as knox_views
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('register/', UserRegistration.as_view(), name="register"),
    path('login/', UserLogin.as_view(), name='login'),
#     path('logout/', knox_views.LogoutView.as_view(), name='logout'),
#     path('admin-user/', AdminPanelView.as_view(), name='admin'),
#     # path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]