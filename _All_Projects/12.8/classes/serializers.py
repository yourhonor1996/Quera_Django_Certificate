# Implement ClassroomSerializer Here
from rest_framework import serializers
from .models import Classroom

class ClassroomSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Classroom
        fields = ('capacity', 'name', 'department', 'area')

    def validate(self, data):
        if data.get('capacity', 0) < 5:
            error = 'Caparity must be more than or equal to 5.'
            raise serializers.ValidationError(error)

        if data.get('area', 0) < 0:
            error = 'Area must be positive value.'
            raise serializers.ValidationError(error)

        return data