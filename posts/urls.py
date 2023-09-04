from django.urls import path

from posts.views.comment import CommentListView, CommentDetailView, CommentCreateView, CommentUpdateView, \
    CommentDeleteView
from posts.views.post import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', PostListView.as_view()),
    path('<int:pk>/', PostDetailView.as_view()),
    path('create/', PostCreateView.as_view()),
    path('<int:pk>/update/', PostUpdateView.as_view()),
    path('<int:pk>/delete/', PostDeleteView.as_view()),
    path('comment/', CommentListView.as_view()),
    path('comment/<int:pk>/', CommentDetailView.as_view()),
    path('comment/create/', CommentCreateView.as_view()),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view()),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view()),
]
