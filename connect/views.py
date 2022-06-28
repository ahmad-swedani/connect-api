from django.shortcuts import render
from .models import Post, Offer, Comment,Activity
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from rest_framework.permissions import IsAuthenticated,AllowAny
from .permissions import (
    IsOwnerOrReadOnly,
    OfferIsOwnerOrReadOnly,
    CommentIsOwnerOrReadOnly,
    ActivityIsOwnerOrReadOnly
)
from .serializers import PostSerializer, OfferSerializer, CommentSerializer,ActivitySerializer


class PostViewsList(ListCreateAPIView):
    queryset = Post.objects.all().order_by("-created_at")
    serializer_class = PostSerializer


class PostDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class OfferViewsList(ListCreateAPIView):
    queryset = Offer.objects.all().order_by("-created_at")
    serializer_class = OfferSerializer


class OfferDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer


class CommentViewsList(ListCreateAPIView):
    queryset = Comment.objects.all().order_by("-created_at")
    serializer_class = CommentSerializer


class CommentDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (CommentIsOwnerOrReadOnly,)
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class ActivityViewsList(ListCreateAPIView):
    queryset = Activity.objects.all().order_by("-created_at")
    serializer_class = ActivitySerializer


class ActivityDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (ActivityIsOwnerOrReadOnly,)
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
