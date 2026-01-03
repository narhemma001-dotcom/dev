from rest_framework import serializers
from .models import PostModel, CommentModel, LikeModel


class PostSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False, allow_null=True)
    owner_username = serializers.ReadOnlyField(source ='owner.username')
    class Meta:
        model = PostModel
        fields = ['id', 'owner','owner_username','content', 'image', 'likes_count', 'comments_count', 'created_at']
        read_only_fields = ['owner', 'owner_username', 'likes_count', 'comments_count', 'created_at']

class CommentSerializer(serializers.ModelSerializer):
    owner_username = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = CommentModel
        fields = ['id', 'post', 'owner','owner_username','content','created_at']  
        read_only_fields = ['post', 'owner']    

class LikeSerializer(serializers.ModelSerializer):
    owner_username = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = LikeModel
        fields = ['id','post','owner','owner_username','created_at']
        read_only_fields = ['post', 'owner']