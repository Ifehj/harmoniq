from django.shortcuts import render
from rest_framework import generics
from .models import CustomUser, Song, Playlist, Likes
from .serializers import CustomUserSerializer, SongSerializer, PlaylistSerializer, LikeSerializer
# Create your views here.

class UserListView(generics.ListAPIView):
	"""View to list all users"""
	queryset = CustomUser.objects.all()
	serializer_class = CustomUserSerializer

class UserDetailView(generics.RetrieveAPIView):
	"""View to retrieve a user by ID"""
	queryset = CustomUser.objects.all()
	serializer_class = CustomUserSerializer

class SongListView(generics.ListAPIView):
	"""View to list all songs"""
	queryset = Song.objects.all()
	serializer_class = SongSerializer

class SongCreateView(generics.CreateAPIView):
	"""View to create a new song"""
	queryset = Song.objects.all()
	serializer_class = SongSerializer

class SongDetailView(generics.RetrieveAPIView):
	"""View to retrieve a song by ID"""
	queryset = Song.objects.all()
	serializer_class = SongSerializer

class PlaylistListCreateView(generics.ListCreateAPIView):
	"""View to list all playlists and create a new playlist"""
	queryset = Playlist.objects.all()
	serializer_class = PlaylistSerializer

class PlaylistDetailView(generics.RetrieveUpdateDestroyAPIView):
	"""View to retrieve a playlist by ID"""
	queryset = Playlist.objects.all()
	serializer_class = PlaylistSerializer

class LikeListCreateView(generics.ListCreateAPIView):
	"""View to list all likes and create a new like"""
	queryset = Likes.objects.all()
	serializer_class = LikeSerializer

class LikeDetailView(generics.RetrieveDestroyAPIView):
	"""View to retrieve a like by ID"""
	queryset = Likes.objects.all()
	serializer_class = LikeSerializer

