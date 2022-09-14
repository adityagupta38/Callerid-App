from rest_framework.serializers import ModelSerializer
from .models import GlobalUsers


class GlobalUsersSerializer(ModelSerializer):
    class Meta:
        model = GlobalUsers
        fields = ('name', 'phoneno', 'spam')
