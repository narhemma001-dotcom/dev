from rest_framework import serializers
from .models import Taskmodel

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Taskmodel
        fields= '__all__'