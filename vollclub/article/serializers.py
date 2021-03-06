from rest_framework import serializers
from .models import Article, Comment, Category

class ArticleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Article
        fields = ('id', 'title', 'description', 'body', 'author_id')

class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = ('id', 'title', 'description', 'created')

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = ('id', 'title', 'description', 'created')


from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']