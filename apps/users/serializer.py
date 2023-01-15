from rest_framework.serializers import ModelSerializer
from .models import CustomUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken


class CustomUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'first_name', 'last_name', 'city',]

    # @classmethod
    # def get_token(cls, user):
    #     token = super().get_token(user)

    #     # Add custom claims
    #     token['email'] = user.email
    #     token['first_name'] = user.first_name
    #     token['last_name'] = user.last_name
    #     token['is_active'] = user.is_active
    #     token['is_staff'] = user.is_staff

    #     return token
    # def create(self, validated_data):
    #     return CustomUser.objects.create_user(**validated_data)

class CustomUserLogin(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'password', ]
   