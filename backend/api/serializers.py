from rest_framework import serializers
from .models import ZenoModel


class ZenoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZenoModel
        fields = '__all__'
