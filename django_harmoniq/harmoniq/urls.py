from django.urls import path, include
from .views import UserListView, UserDetailView, SongListView, SongCreateView, SongDetailView, PlaylistListCreateView, PlaylistDetailView, LikeListCreateView, LikeDetailView

urlpatterns = [
	# Users
	path('users/', UserListView.as_view(), name='user-list'),
	path('users/<int:pk>', UserDetailView.as_view(),name='user-detail'),

	# Songs
	path('songs/', SongListView.as_view(), name='song-list'),
	path('songs/<int:pk>', SongDetailView.as_view(), name='song-detail'),
	path('song/create/', SongCreateView.as_view(), name='song-create'),

	# Playlists
	path('playlist/list-create/', PlaylistListCreateView.as_view(), name='playlist'),
	path('playlist/<int:pk>', PlaylistDetailView.as_view(), name='playlist-detail'),

	# Likes
	path('likes/', LikeListCreateView.as_view(), name='like-list'),
	path('likes/<int:pk>', LikeDetailView.as_view(), name='like-detail')


]