from django.db.models import fields
from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        
        fields = (
            'username',
            'password',
            'phone',
            'address',
            'gender',
            'age',
            'description',
            'first_name', 
            'last_name',
            'email')
    # if we don't implement this create method, the obtain_auth_token view won't work 
    # because the default serializer doesn't save the passwords as hash and we have to make this happen
    # by using the set_password function. 
    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
