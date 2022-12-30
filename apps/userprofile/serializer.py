from rest_framework.serializers import ModelSerializer
from .models import UserProfileModel

class UserProfileSerializer(ModelSerializer):
    class Meta: 
        model = UserProfileModel
        fields = '__all__'