from rest_framework import serializers

from blog.api.models import Blog, Category, Comment


class BlogSerializer(serializers.ModelSerializer):
  class Meta:
    model = Blog
    fields = ['id','title', 'body','image','date_updated']
    # 


class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Comment
    fields = '__all__'