from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import BlogSerializer, CategorySerializer, CommentSerializer 
from .models import Blog, Category, Comment
from django.shortcuts import get_object_or_404



def home(request):
  return HttpResponse("Tito is my name ",request)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def Blog_lists(request):
  user = request.user

  try:
    blog = user.blog_set.all()
    # blog = Blog.objects.all()
  except Blog.DoseNotExist:
    return Response(status = status.Http_404_NOT_FOUND)
  if request.method == 'GET':
        # blog = Blog.objects.all()
        serializer = BlogSerializer(blog, many=True)
        return Response(serializer.data)

@api_view(['PUT'])
def update_Blog_list(request, id):

  try:
    blog = Blog.objects.get(pk=id)
  except Blog.DoseNotExist:
    return Response(status = status.Http_404_NOT_FOUND)
  if request.method == 'PUT':
        # blog = Blog.objects.all()
        serializer = BlogSerializer(blog, data=request.data)
        data = {}
        if serializer.is_valid():
          serializer.save()
          data["Success"] = "Updated Successfully"
          return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_Blog(request, id):

  try:
    blog = Blog.objects.get(pk=id)
  except Blog.DoseNotExist:
    return Response(status = status.Http_404_NOT_FOUND)
  if request.method == 'DELETE':
        operations =  blog.delete()
        data = {}
        if operations:
          data["Success"] = "Deleted Successfully"
        else:
          data["Failed"] = "Failed to Delete"

        return Response(data=data)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def create_blog(request):
  if request.method == 'POST':
        serializer = BlogSerializer(data = request.data)
        if serializer.is_valid():
          serializer.save()
          return Response(serializer.data, status = status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def get_category_list(request):

  try:
    category = Category.objects.all()
  except Category.DoesNotExist:
    return Response(status = status.Http_404_NOT_FOUND)
  if request.method =='GET':
    serializer = CategorySerializer(category, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_category(request, id):

   try:
    category = Category.objects.get(pk=id)
   except Category.DoesNotExist:
     return Response(status = status.Http_404_NOT_FOUND)
   if request.method =='GET':
    serializer = CategorySerializer(category)
    return Response(serializer.data)


@api_view(['POST'])
def create_category(request):
  if request.method == 'POST':
        serializer = CategorySerializer(data = request.data)
        if serializer.is_valid():
          serializer.save()
          return Response(serializer.data, status = status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['PUT']) 
def update_category(request, id):

  try:
    category = Category.objects.get(pk=id)
  except Category.DoesNotExist:
    return Response(status=status.HTTP_400_BAD_REQUEST)
  if request.method == 'PUT':
    serializer = CategorySerializer(category, data = request.data)
    data={}
    if serializer.is_valid():
          serializer.save()
          data["Success"] = "Updated Successfully"
          return Response(data=data)
            # serializer.data, status = status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['DELETE'])  
def delete_category(request, id):

  try:
    category = Category.objects.get(pk=id)
  except Category.DoesNotExist:
    return Response(status = status.Http_404_NOT_FOUND)  
  if request.method == 'DELETE':
    operations =  category.delete()

    data = {}

    if operations:
      data["Success"] ="Deleted Successfully"
    else:
      data["Failed"] = "Failed to delete"

    return Response(data=data)



@api_view(['POST'])
def create_comment(request):
  if request.method == 'POST':
        serializer = CommentSerializer(data = request.data)
        if serializer.is_valid():
          serializer.save()
          return Response(serializer.data, status = status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_comments_list(request):

  try:
    Comment = Comment.objects.all()
  except Comment.DoesNotExist:
    return Response(status = status.Http_404_NOT_FOUND)
  if request.method =='GET':
    serializer = CommentSerializer(Comment, many=True)
    return Response(serializer.data)


@api_view(['DELETE'])  
def delete_comment(request, id):

  try:
    comment = Comment.objects.get(pk=id)
  except Comment.DoesNotExist:
    return Response(status = status.Http_404_NOT_FOUND)  
  if request.method == 'DELETE':
    operations =  comment.delete()

    data = {}

    if operations:
      data["Success"] ="Deleted Successfully"
    else:
      data["Failed"] = "Failed to delete"

    return Response(data=data)

@api_view(['POST'])
def like_create_api(request, id):
    blog = get_object_or_404(Blog.objects.all(), pk=id)
    blog.likers.add(request.user)
    serializer = BlogSerializer(blog)
    return Response(serializer.data, status=status.HTTP_201_CREATED)