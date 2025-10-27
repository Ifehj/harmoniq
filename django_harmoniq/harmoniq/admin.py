from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Song, Playlist, Likes


# ==========================
# Custom User Admin
# ==========================
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'role', 'is_active', 'is_staff', 'date_joined')
    list_filter = ('role', 'is_active', 'is_staff')
    search_fields = ('username', 'email')
    ordering = ('-date_joined',)

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal Info', {'fields': ('role',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'role', 'password1', 'password2'),
        }),
    )


# ==========================
# Song Admin
# ==========================
@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'release_date')
    search_fields = ('title', 'artist__username')
    list_filter = ('release_date',)
    ordering = ('-release_date',)


# ==========================
# Playlist Admin
# ==========================
@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'is_public', 'created_at')
    search_fields = ('name', 'owner__username')
    list_filter = ('is_public', 'created_at')
    ordering = ('-created_at',)
    filter_horizontal = ('songs',)


# ==========================
# Likes Admin
# ==========================
@admin.register(Likes)
class LikesAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'song_id', 'liked_at')
    search_fields = ('user_id__username', 'song_id__title')
    list_filter = ('liked_at',)
    ordering = ('-liked_at',)
