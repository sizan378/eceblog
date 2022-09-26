
from django.urls import path
from .views import ArticleListView, ArticleDetailView, CategoryView

urlpatterns = [
    path('', ArticleListView.as_view()),
    path('<int:pk>/', ArticleDetailView.as_view()),
    path('category/', CategoryView.as_view(), name='category_list'),
]