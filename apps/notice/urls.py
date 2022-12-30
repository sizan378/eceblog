
from django.urls import path
from .views import NoticeDetailView, NoticeListView

urlpatterns = [
    path('', NoticeListView.as_view()),
    path('<int:pk>/', NoticeDetailView.as_view()),
]