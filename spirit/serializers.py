from rest_framework import serializers
from .models import Spirit

class SpiritSerializers(serializers.ModelSerializer):
    class Meta:
        model = Spirit
        fields = ['id', 'name', 'description']


