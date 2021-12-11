from allauth.account.utils import setup_user_email
from rest_framework.serializers import ModelSerializer
from allauth.account.adapter import get_adapter
from project_app import settings
from .models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

   class Meta:
      model = User
      fields = "__all__"
