from rest_framework import serializers
from .models import User

class UserRegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length = 120)
    email = serializers.EmailField(
        max_length=100,
        min_length=5,
        required=True,
        allow_blank=False,
        error_messages={
            'required': 'Email is required',
            'invalid': 'Enter a valid email address'
        })
    password = serializers.CharField(max_length = 128, min_length=8, write_only=True, label="Password")
    password2 = serializers.CharField(max_length = 128, min_length=8, write_only=True, label="Confirm Password")
    
    class Meta:
        model = User
        fields = ['is_admin', 'username', 'email', 'password', 'password2']

    def validate(self, data):
        password = data['password']
        password2 = data['password2']
        if password != password2:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return data
    
    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create_user(**validated_data)
        return user
    
class UserProfileserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']