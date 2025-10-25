from rest_framework import serializers 
from .models import CustomUser, Song, Playlist, Likes
from django.contrib.auth import authenticate

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

class RegisterSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True)

	class Meta:
		model = CustomUser
		fields = ['username', 'email', 'password', 'role']

	def create(self, validated_data):
		user = CustomUser.objects.create_user(
			username = validated_data['username'],
			email = validated_data.get('email'),
			password=validated_data['password'],
			role=validated_data.get('role', 'Listener')
		)
		return user

class LoginSerializer(serializers.Serializer):
	username = serializers.CharField()
	password = serializers.CharField(write_only=True)

	def validate(self, data):
		username = data.get('username')
		password = data.get('password')

		if username and password:
			user = authenticate(username=username, password=password)
			if not user:
				raise serializers.ValidationError("Unable to log in with provided credentials.")
		else:
			raise serializers.ValidationError("Must include 'username' and 'password'.")

		data['user'] = user
		return data