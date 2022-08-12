from .models import Poem
from rest_framework import serializers

class PoemSerializer(serializers.ModelSerializer):
    class Meta():
        model = Poem
        fields = '__all__'
        
# class GenreSerializer(serializers.ModelSerializer):
#     class Meta():
#         model = Genre
#         fields = '__all__'