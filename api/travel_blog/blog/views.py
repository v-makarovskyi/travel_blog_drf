
from unicodedata import category
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import generics
from blog.models import Post, Comment, Category
from .serializers import PostSerializer, CommentSerializer, CategorySerializer
from rest_framework.permissions import AllowAny, SAFE_METHODS, IsAuthenticated, IsAuthenticatedOrReadOnly, BasePermission, IsAdminUser, DjangoModelPermissions
from .permissions import IsOwnerOrReadOnly
from rest_framework.response import Response
from rest_framework import status


class HomeView(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CategoryPostList(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.prefetch_related('posts').filter(level=1)  


    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, slug=self.kwargs.get('slug'))
        return obj
    
        
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    lookup_field = 'slug'
    lookup_url_kwarg = 'post_slug'


class CommentsList(generics.ListCreateAPIView, IsOwnerOrReadOnly):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    

    