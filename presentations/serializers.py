from rest_framework import serializers
from .models import Prezi, Creator

class CreatorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Creator
        fields = "__all__"

class PreziSerializer(serializers.ModelSerializer):
    creator = CreatorSerializer()
    class Meta:
        model = Prezi
        fields = "__all__"