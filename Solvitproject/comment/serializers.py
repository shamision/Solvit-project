from rest_framework import serializers
from .models import *

class comment_serializer(serializers.ModelSerializer):
    class Meta:
        model = comment_model
        fields = '__all__'