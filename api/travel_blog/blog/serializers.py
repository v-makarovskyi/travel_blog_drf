from rest_framework import serializers
from .models import Post, Comment, Category, Tag
from users.serializers import MyUserSerializer


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    
    class Meta:
        model = Comment
        fields = ['owner', 'text', 'post']
    
    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    comments = CommentSerializer(many=True, read_only=True)
    category = serializers.ReadOnlyField(source='category.slug')
    tags = TagSerializer(many=True, read_only=True)
   
    class Meta:
        model = Post
        fields = ['id', 'category', 'title', 'image', 'text', 'tags', 'slug', 'owner', 'created', 'comments']


    
class CategorySerializer(serializers.ModelSerializer):

    posts = PostSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'title', 'slug', 'image', 'description', 'posts']
        depth = 2
