
from django.urls import path

from .views import CommentListView, CommentUpdateView

urlpatterns = [
    path('', CommentListView.as_view()),
    path('<int:pk>/', CommentUpdateView.as_view()),
]
