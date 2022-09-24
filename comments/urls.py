
from django.urls import path
from comments.views import ListCreateAPIView, RetrieveUpdateAPIView

urlpatterns = [
    path('', ListCreateAPIView.as_view()),
    path('<int:pk>/', RetrieveUpdateAPIView.as_view()),
]