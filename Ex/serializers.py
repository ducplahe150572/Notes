from rest_framework import serializers
from Ex.models import Notes


class ExSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = ['name']