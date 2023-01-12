from django.shortcuts import render
from rest_framework import generics
from rest_framework import generics, permissions
from .models import Category, Post
from . import serializers
# Create your views here.


class PostListCreateView(generics.ListAPIview):
    queryset = Post.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly)
    serializer_class = serializers.PostListSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return serializers.PostListSerializer
        return serializers.PostCreateSerializer


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()

    def get_serializer_class(self):
        if self.request.method in ('PUT', 'PATCH'):
            return serializers.PostCreateSerializer
        return Post