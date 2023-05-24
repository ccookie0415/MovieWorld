from rest_framework import serializers
from .models import Profile, Guestbook


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Profile
        fields = '__all__'
        read_only_fields = ('user', 'followings')

class GuestbookSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Guestbook
        fields = '__all__'
        read_only_fields = ('user', 'author')