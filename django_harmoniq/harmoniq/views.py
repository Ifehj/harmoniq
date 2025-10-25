from rest_framework import permissions
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser, Song, Playlist, Likes
from .serializers import CustomUserSerializer, SongSerializer, PlaylistSerializer, LikeSerializer, RegisterSerializer, LoginSerializer
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from .permissions import IsArtist, IsAdmin
# Create your views here.


class UserListView(generics.ListAPIView):
	"""View to list all users"""
	queryset = CustomUser.objects.all()
	serializer_class = CustomUserSerializer
	permission_classes = [IsAdmin]

class UserDetailView(generics.RetrieveAPIView):
	"""View to retrieve a user by ID"""
	queryset = CustomUser.objects.all()
	serializer_class = CustomUserSerializer
	permission_classes = [IsAdmin]

class SongListView(generics.ListAPIView):
	"""View to list all songs"""
	queryset = Song.objects.all()
	serializer_class = SongSerializer
	permission_classes =[permissions.AllowAny]

class SongDetailView(generics.RetrieveAPIView):
	"""View to retrieve a song by ID"""
	queryset = Song.objects.all()
	serializer_class = SongSerializer
	permission_classes =[permissions.AllowAny]

class PlaylistListCreateView(generics.ListCreateAPIView):
	"""View to list all playlists and create a new playlist"""
	queryset = Playlist.objects.all()
	serializer_class = PlaylistSerializer

class PlaylistDetailView(generics.RetrieveUpdateDestroyAPIView):
	"""View to retrieve a playlist by ID"""
	queryset = Playlist.objects.all()
	serializer_class = PlaylistSerializer


class LikeDetailView(generics.RetrieveDestroyAPIView):
	"""View to retrieve a like by ID"""
	queryset = Likes.objects.all()
	serializer_class = LikeSerializer

class RegisterView(generics.CreateAPIView):
	"""View to Register a new user"""
	queryset = CustomUser.objects.all()
	serializer_class = RegisterSerializer
	permission_classes = [permissions.AllowAny, IsArtist]

	def create(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		user = serializer.save()
		token, created = Token.objects.get_or_create(user=user)
		return Response({
            "user": CustomUserSerializer(user).data,
            "token": token.key
        }, status=status.HTTP_201_CREATED)

class LoginView(APIView):
	"""View to Login a user"""
	serializer_class = LoginSerializer
	permission_classes = [permissions.AllowAny]

	def post(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		user = serializer.validated_data['user']
		token, created = Token.objects.get_or_create(user=user)
		return Response({
			"user": CustomUserSerializer(user).data,
			"token": token.key
		}, status=status.HTTP_200_OK)
	
class LogoutView(APIView):
	"""View to Logout a user"""
	def post(self, request, *args, **kwargs):
		request.user.auth_token.delete()
		return Response({
			'message': 'Successfully logged out.'
		}, status=status.HTTP_200_OK)

class LikeSongView(APIView):

	def post(self, request, pk):
		user = request.user
		song = get_object_or_404(Song, pk=pk)

		if Likes.objects.filter(user=user, song=song).exists():
			return Response({"detail": "You have already liked this song."}, status=status.HTTP_400_BAD_REQUEST)
		
		Likes.objects.create(user=user, song=song)
		return Response({"message": "Song liked successfully."}, status=status.HTTP_201_CREATED)

class UnlikeSongView(APIView):

	def post(self, request, pk):
		user = request.user
		song = get_object_or_404(Song, pk=pk)

		like = Likes.objects.filter(user=user, song=song).first()
		if not like:
			return Response({"detail": "You have not liked this song."}, status=status.HTTP_400_BAD_REQUEST)
		
		like.delete()
		return Response({"message": "Song unliked successfully."}, status=status.HTTP_200_OK)
	
class PlaylistAddSongView(APIView):
	"""View to add a song to a playlist"""

	def post(self, request, pk):
		user = request.user
		song = get_object_or_404(Song, pk=pk)

		if Playlist.objects.filter(user=user, song=song).exists():
			return Response({"Message": "Song is already in playlist"}, status=status.HTTP_400_BAD_REQUEST)

		playlist_entry = Playlist.object.create(user=user, song=song)

		return Response({
			"Message": "Song added to playlist",
			"playlist_entry_id": playlist_entry.id
			}, status=status.HTTP_201_CREATED)
	
class PlaylistRemoveSongView(APIView):
	"""View to remove a song from a playlist"""

	def post(self, request, pk):
		user = request.user
		song = get_object_or_404(Song, pk=pk)

		playlist_entry = Playlist.objects.filter(user=user, song=song).first()
		if not playlist_entry:
			return Response({"Message": "Song not found in playlist"}, status=status.HTTP_400_BAD_REQUEST)

		playlist_entry.delete()

		return Response({"Message": "Song removed from playlist"}, status=status.HTTP_200_OK)

class SongUploadView(generics.CreateAPIView):
	"""View to upload a new song file"""
	queryset = Song.objects.all()
	serializer_class = SongSerializer
	permission_classes = [permissions.IsAuthenticated]

	def perform_create(self, serializer):
		serializer.save(uploaded_by=self.request.user)

class PublicPlaylistView(generics.ListAPIView):
	"""View to get public playlists"""
	queryset = Playlist.objects.filter(is_public=True)
	serializer_class = PlaylistSerializer
	permission_classes =[permissions.AllowAny]

class SongsByGenreView(generics.ListAPIView):
	"""View to list songs by genre"""
	serializer_class = SongSerializer
	permission_classes =[permissions.AllowAny]
	def get_queryset(self):
		genre = self.kwargs.get('genre')  # get 'genre' from URL
		return Song.objects.filter(genre__iexact=genre)  # case-insensitive match