from django.shortcuts import render
from rest_framework import viewsets
from .serializer import BlogSerializer
from news.models import Blog
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class BlogDetailsData(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]  # allows authentication/ must login into admin first
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
