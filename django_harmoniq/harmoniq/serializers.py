from rest_framework import serializers 
from .models import CustomUser, Song, Playlist, Likes

class CustomUserSerializer(serializers.ModelSerializer):
	class Meta:
		model = CustomUser
		fields =['id', 'username', 'email', 'role', 'date_joined']

class SongSerializer(serializers.ModelSerializer):
	artist = CustomUserSerializer(read_only=True)

	class Meta:
		model = Song
		fields = ['id', 'title', 'artist', 'audio_file', 'cover_image', 'release_date']
	
class PlaylistSerializer(serializers.ModelSerializer):
	owner = CustomUserSerializer(read_only=True)
	songs = SongSerializer(many=True, read_only=True)

	class Meta:
		model = Playlist
		fields = ['id','name', 'owner', 'songs', 'created_at', 'is_public']

class LikeSerializer(serializers.ModelSerializer):
	user = CustomUserSerializer(read_only=True)
	song = SongSerializer(read_only=True)

	class Meta:
		model = Likes
		fields = ['id', 'user', 'song', 'liked_at']