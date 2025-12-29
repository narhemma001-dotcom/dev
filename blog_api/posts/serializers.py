from rest_framework import serializers
from .models import PostModel

class PostModelSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    class Meta:
        model = PostModel
        fields = "__all__"
        read_only_fields = ['created_at','author', 'updated_at']