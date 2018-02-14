# -*- coding: utf-8 -*-

# Django
from rest_framework import serializers


class AuthCustomTokenSerializer(serializers.Serializer):
    user = serializers.CharField()
    password = serializers.CharField(style={'input_type': 'password'})


class UsersSerializer(serializers.Serializer):
    user = serializers.CharField()
    password = serializers.CharField(style={'input_type': 'password'})
    password2 = serializers.CharField(style={'input_type': 'password'})
