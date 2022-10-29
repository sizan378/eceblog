
from django.urls import path
from comments.views import CommentsListView, CommentsRetrieveView

urlpatterns = [
    path('', CommentsListView.as_view(), name='comments_list'),
    path('<int:pk>/', CommentsRetrieveView.as_view(), name='comments_update'),
]
