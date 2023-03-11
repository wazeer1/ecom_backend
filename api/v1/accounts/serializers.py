from django.conf import settings
from django.conf import settings as SETTINGS
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class SignUpserializer(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.CharField()
    phone = serializers.CharField()
    username = serializers.CharField()
    password = serializers.CharField()
    country = serializers.CharField()

class Verifyserializer(serializers.Serializer):
    email = serializers.CharField()
    phone = serializers.CharField()
    country = serializers.CharField()
    otp = serializers.CharField()


class Loginserializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()