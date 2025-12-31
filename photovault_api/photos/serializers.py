from rest_framework import serializers
from .models import Photo

class PhotoSerializer(serializers.ModelSerializer):
    owner_username = serializers.ReadOnlyField(source='owner.username')  # Show owner's username
    owner_id = serializers.ReadOnlyField(source='owner.id')  # Show owner's ID
    
    class Meta:
        model = Photo
        fields = [
            'id', 
            'owner_id',
            'owner_username',
            'title', 
            'description', 
            'image', 
            'visibility', 
            'created_at', 
            'updated_at'
        ]
        read_only_fields = ['owner_id', 'owner_username', 'created_at', 'updated_at']
    
    def create(self, validated_data):
        # The owner will be set in the view
        return Photo.objects.create(**validated_data)