from .models import *
from .serializers import *
from rest_framework import serializers
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Create your views here.

# class createViewGenre(generics.ListCreateAPIView):
#     queryset = Genre.objects.all()
#     serializer_class = GenreSerializer
# class editDeleteGenre(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Genre.objects.all()
#     serializer_class = GenreSerializer
    
class createPoem(generics.CreateAPIView):
    permission_classes=[IsAuthenticatedOrReadOnly]
    queryset = Poem.objects.all()
    serializer_class = PoemSerializer
    
class viewPoem(generics.ListAPIView):
    permission_classes=[IsAuthenticatedOrReadOnly]
    queryset = Poem.objects.all()
    serializer_class= PoemSerializer
    
class editPoem(generics.UpdateAPIView):
    permission_classes=[IsAuthenticatedOrReadOnly]
    queryset = Poem.objects.all()
    serializer_class = PoemSerializer
    
class deletePoem(generics.DestroyAPIView):
    permission_classes=[IsAuthenticatedOrReadOnly]
    queryset = Poem.objects.all()
    serializer_class = PoemSerializer