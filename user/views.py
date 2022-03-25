from rest_framework import viewsets

from user.models import UserModel
from user.serializers import UserSerializer
# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer



