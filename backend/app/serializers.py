from rest_framework import serializers
from .models import Property


class PropertySerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M")

    class Meta:
        model = Property
        fields = ('id', 'title', 'buildingName', 'buildingType', 'price', 'entranceImage', 'exteriorImage', 'floorPlan', 'transportation', 'address', 'showerRoomAndBathRoom', 'kitchen', 'Feature', 'created_at')
