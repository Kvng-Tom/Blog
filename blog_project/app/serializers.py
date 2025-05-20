from rest_framework import serializers
from .models import *




class AuthorSerializer(serializers.ModelSerializer):
    
      
    class Meta:
        model = Author
        fields = '__all__'


# class MiniBlogSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Blog
#         fields = ['id', 'title', 'created_at']


class Blogserializer(serializers.ModelSerializer):

    author_data = serializers.ReadOnlyField()

    class Meta:
        model = Blog
        fields = '__all__'