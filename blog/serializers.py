from rest_framework import serializers
from .models import Post, Category
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields= ['id', 'title', 'created_at'] 

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields= ['id','title', 'body', "category" ,'created_at'] 
   