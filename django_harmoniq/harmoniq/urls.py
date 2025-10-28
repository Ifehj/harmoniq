from django.urls import path, include
from .views import UserListView, UserDetailView, SongListView, SongDetailView, PlaylistListCreateView, PlaylistDetailView, LikeDetailView, RegisterView, LoginView, LogoutView, PlaylistAddSongView, PlaylistRemoveSongView, SongUploadView, PublicPlaylistView, LikeSongView, UnlikeSongView

urlpatterns = [
	# Users
	path('users/', UserListView.as_view(), name='user-list'),
	path('users/<int:pk>', UserDetailView.as_view(),name='user-detail'),

	# Songs
	path('songs/', SongListView.as_view(), name='song-list'),
	path('songs/<int:pk>', SongDetailView.as_view(), name='song-detail'),

	# Playlists
	path('playlist/list-create/', PlaylistListCreateView.as_view(), name='playlist'),
	path('playlist/<int:pk>', PlaylistDetailView.as_view(), name='playlist-detail'),
	path('playlist/<int:playlist_id>/add-song/<int:song_id>/', PlaylistAddSongView.as_view(), name='playlist-add-song'),
	path('playlist/<int:playlist_id>/remove-song/<int:song_id>/', PlaylistRemoveSongView.as_view(), name='playlist-remove-song'),
	path('public-playlists/', PublicPlaylistView.as_view(), name='public-playlists'),

	# Likes
	path('likes/<int:pk>', LikeDetailView.as_view(), name='like-detail'),
	path('song/<int:pk>/like/', LikeSongView.as_view(), name='song-like'),
	path('song/<int:pk>/unlike/', UnlikeSongView.as_view(), name='song-unlike'),

	# Registration
	path('register/', RegisterView.as_view(), name='register'),

	# Authentication
	path('login/', LoginView.as_view(), name='login'),
	path('logout/', LogoutView.as_view(), name='logout'),

	# Upload song
	path('song/upload/', SongUploadView.as_view(), name='song-upload'),
]