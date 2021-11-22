from .models import Pin, Save
from rest_framework import serializers
from project import settings
from accounts.models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'avatar')

class PinSerializer(serializers.ModelSerializer):
    creator = UserSerializer()
    class Meta:
        model = Pin
        fields = '__all__'


class PinCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pin
        fields = '__all__'
class PinSaveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Save
        fields = '__all__'