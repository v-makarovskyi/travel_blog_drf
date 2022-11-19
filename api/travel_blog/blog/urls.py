from django.urls import path
from .views import HomeView, PostDetail, CommentDetail, CategoryPostList, CommentsList 

app_name = 'blog'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('comments/', CommentsList.as_view()),
    path('comments/<int:pk>/', CommentDetail.as_view(), name='create_comment'),
    path('<slug:slug>/', CategoryPostList.as_view(), name='post_list'),
    path('<slug:slug>/<slug:post_slug>/', PostDetail.as_view(), name='post_single'),
]