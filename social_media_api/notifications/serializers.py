from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    actor_username = serializers.CharField(source="actor.username", read_only=True)
    target_info = serializers.SerializerMethodField()

    class Meta:
        model = Notification
        fields = [
            'id',
            'recipient',
            'actor',
            'actor_username',
            'verb',
            'target_info',
            'timestamp',
            'read',
        ]

    def get_target_info(self, obj):
        if obj.target:
            return str(obj.target)
        return None