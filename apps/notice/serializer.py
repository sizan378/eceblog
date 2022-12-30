from rest_framework.serializers import ModelSerializer
from .models import NoticeModel


class NoticeSerializer(ModelSerializer):
    class Meta:
        model = NoticeModel
        fields = '__all__'