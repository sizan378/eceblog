
from django.urls import path
from post.views import ArticleListView, ArticleDetailView, CategoryView, CategoryUpdateView

urlpatterns = [
    path('', ArticleListView.as_view()),
    path('<int:pk>/', ArticleDetailView.as_view()),

    # Category Update,List and Create URLS
    path('category/', CategoryView.as_view(), name='category_list'),
    path('category/<int:pk>/', CategoryUpdateView.as_view(), name='category_update'),
]
