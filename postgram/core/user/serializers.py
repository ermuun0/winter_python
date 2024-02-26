from rest_framework import serializers
from core.user.models import User
from core.abstract.serializers import AbstractSerializer

class UserSerializer(AbstractSerializer):
    posts_count = serializers.SerializerMethodField()
    def get_posts_count(self, instance):
        return instance.post_set.all().count()
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name',
            'last_name', 'bio', 'avatar', 'email',
            'is_active', 'created', 'updated']
        read_only_field = ['is_active']


    