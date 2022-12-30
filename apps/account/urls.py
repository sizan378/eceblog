
from .views import RegisterAPI, LoginAPI, AdminPanelView
from knox import views as knox_views
from django.urls import path

urlpatterns = [
    path('register/', RegisterAPI.as_view()),
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('admin-user/', AdminPanelView.as_view(), name='admin'),
    # path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]