
from django.urls import path
<<<<<<< HEAD
from comments.views import CommentsListView, CommentsRetrieveView

urlpatterns = [
    path('', CommentsListView.as_view(), name='comments_list'),
    path('<int:pk>/', CommentsRetrieveView.as_view(), name='comments_update'),
]
=======
from comments.views import CommentListView, CommentUpdateView

urlpatterns = [
    path('', CommentListView.as_view()),
    path('<int:pk>/', CommentUpdateView.as_view()),
]
>>>>>>> c638cfd2ee87711ba98f489361583b664058678b
