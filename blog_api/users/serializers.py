from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

class UserCreateSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required= True,
        validators= [UniqueValidator(queryset= User.objects.all())]
    )
    password = serializers.CharField(write_only= True, min_length= 8)
    password2 = serializers.CharField(write_only= True, label= "Confirm Password")    

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            'username': {
                'validators': [UniqueValidator(queryset= User.objects.all())]
            }
        }
    
    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({
                "password": "Passwords don't match"
            })
        return data    

    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create_user(
            username= validated_data['username'],
            email= validated_data['email'],
            password = validated_data['password']
        )    
        return user