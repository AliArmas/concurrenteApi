from rest_framework import viewsets
from photo.models import PhotoModel

from photo.serializers import PhotoSerializer
# Create your views here.
class PhotoViewSet(viewsets.ModelViewSet):
    queryset = PhotoModel.objects.all()
    serializer_class = PhotoSerializer
