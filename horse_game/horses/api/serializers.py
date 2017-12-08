from rest_framework import serializers
from horses.models import Horse

class HorseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horse
        fields = ('id', 'name', 'age', 'breed', 'color', 'owner', 'created_at', 'updated_at')


