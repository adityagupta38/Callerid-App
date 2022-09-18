from rest_framework import serializers
from .models import GlobalUsers
import re


class GlobalUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = GlobalUsers
        fields = ('name', 'phoneno', 'spam')

    def validate_phoneno(self, phoneno):
        regex = re.compile(r'\d+')
        if not re.match(regex, phoneno):
            raise serializers.ValidationError('Phoneno Should Contain digits from 0 to 9')
        return phoneno
