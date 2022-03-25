from rest_framework import serializers

from photo.models import PhotoModel

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoModel
        fields = ('url')

