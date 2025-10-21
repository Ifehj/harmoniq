from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
# Create your models here.

"""Create Custom User Manager"""
class CustomUserManager(BaseUserManager):
	def create_user(self, email, username, password=None, **extra_fields):
		"""Created and saves a username with given data fields"""

		if not username:
			raise ValueError("User must have a username")
		if not email:
			raise ValueError("User must have an email address")

		email = self.normalize_email(email)
		user = self.model(email=email, username=username, **extra_fields)
		user.set_password(password)
		user.save(using=self._db)
		return user
	
	def create_superuser(self, email, username, password=None, **extra_fields):	
		"""Create and saves a superuser with given data fields"""
		extra_fields.setdefault('is_staff', True)
		extra_fields.setdefault('is_superuser', True)

		if extra_fields.get('is_staff') is not True:
			raise ValueError("Superuser must have is_staff=True.")
		if extra_fields.get('is_superuser') is not True:
			raise ValueError("Superuser must have is_superuser=True.")

		return self.create_user(email, username, password, **extra_fields)

class CustomUser(AbstractUser):
	ROLE_CHOICES = [
		('Artist', 'Artist'),
		('Listener', 'Listener'),
	]

	role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Listener')

	def __str__(self):
		return self.username
	
class Song(models.Model):
	title = models.CharField(max_length=200)
	artist = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='songs')
	audio_file = models.FileField(upload_to='songs/audiofiles/')
	cover_image = models.ImageField(upload_to='songs/coverimages/', null=True, blank=True)
	release_date = models.DateField(auto_now_add=True)


	def __str__(self):
		return f"{self.title} by {self.artist.username}"
	
class Playlist(models.Model):
	name = models.CharField(max_length=100)
	owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='playlists')
	songs = models.ManyToManyField(Song, related_name='playlists')
	created_at = models.DateTimeField(auto_now_add=True)
	is_public = models.BooleanField(default=False)

	def __str__(self):
		return f"Playlist: {self.name} by {self.owner.username}"
	
class Likes(models.Model):
	user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='liked_songs')
	song_id = models.ForeignKey(Song, on_delete=models.CASCADE, related_name='likes')
	liked_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.user.username} likes {self.song.title}"
