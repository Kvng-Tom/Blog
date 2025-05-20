from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework.decorators import api_view
# from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet

# Create your views here.

# @api_view(['POST'])
# def create_author(request):

#     serializer = AuthorSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)

#     serializer.save()

#     return Response(serializer.data, status=200)


# class GetAuthors(APIView):

#     def get(self, request):

#         authors = Author.objects.all().order_by('id')

#         serializer = AuthorSerializer(authors, many=True)

#         return Response(serializer.data, status = 200)


# @api_view(['GET'])

# def get_author_by_id(request, id):

#     author = get_object_or_404(Author, id=id)

#     serializer = AuthorSerializer(author)

#     return Response(serializer.data, status=200)


# @api_view(['POST'])
# def create_blog(request):

#     serializer = Blogserializer (data=request.data)
#     serializer.is_valid(raise_exception=True)

#     serializer.save()

#     return Response(serializer.data, status=201)


# class GetBlogs(APIView):

#     def get(self, request):

#         blogs = Blog.objects.all().order_by('id')

#         serializer = Blogserializer (blogs, many=True)

#         return Response(serializer.data, status = 200)

class AuthorViewSet(ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class BlogViewSet(ModelViewSet):
    serializer_class = Blogserializer    
    queryset = Blog.objects.all()

@api_view(['GET'])
def authors_blog(request, pk):

    try:

        author = Author.objects.get(id=pk)
    
    except Author.DoesNotExist:

        return Response({
            "error" : f"Author {pk} not found"
        }, status =404)

    blogs = Blog.objects.filter(author=author)

    serializer = Blogserializer(blogs, many=True)

    return Response(serializer.data, status=200)


def example_view(request):
    return render(request, 'index.html')
