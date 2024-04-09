from rest_framework import serializers

from app.models import ElementModel


class ElementModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElementModel
        fields = "__all__"
