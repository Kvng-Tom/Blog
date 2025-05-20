from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
from .views import example_view

router = DefaultRouter()
router.register(r'authors', AuthorViewSet, basename='author')
router.register(r'blogs', BlogViewSet, basename='blog')


urlpatterns = [

path('', include(router.urls)),
path('authors_blogs/<int:pk>/', authors_blog),
path('sample/', example_view),





#     path('create-author/', create_author),
#     path('get-authors/', GetAuthors.as_view()),
#     path('get-authors/<int:id>/', get_author_by_id),
#     path('create-blog/', create_blog),
#     path('get-blogs/', GetBlogs.as_view()),



]