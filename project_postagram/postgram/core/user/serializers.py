from rest_framework import serializers
from core.user.models import User
from core.abstract.serializers import AbstractSerializer
from django.conf import settings

class UserSerializer(AbstractSerializer):
    posts_count = serializers.SerializerMethodField()
    def get_posts_count(self, instance):
        return instance.post_set.all().count()
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name',
            'last_name', 'avatar', 'email', 'created', 'updated', 'posts_count']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if not representation['avatar']:
            representation['avatar'] = settings.DEFAULT_AUTO_FIELD
            return representation
        if settings.DEBUG: # debug enabled for dev
            request = self.context.get('request')
            representation['avatar'] =request.build_absolute_uri(representation['avatar'])
            return representation


    