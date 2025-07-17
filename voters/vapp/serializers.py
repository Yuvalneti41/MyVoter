from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Politikai, Goverment


class UserRegisterationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']
        
    def create(self, validated_data):
        user = User(
            username = validated_data['username'],
            email = validated_data['email'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class PolitikaiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Politikai
        fields = '__all__'


class GovermentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goverment
        fields = '__all__'