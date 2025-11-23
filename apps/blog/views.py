from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import BlogPostSerializer
from .models import BlogPost


class BlogListViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """

    def list(self, request):
        queryset = BlogPost.objects.all()
        serializer = BlogPostSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = BlogPost.objects.all()
        blog_post = get_object_or_404(queryset, pk=pk)
        serializer = BlogPostSerializer(blog_post)
        return Response(serializer.data)
