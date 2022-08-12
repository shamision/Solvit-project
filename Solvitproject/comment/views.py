from rest_framework import generics
from .models import comment_model
from .serializers import comment_serializer
from rest_framework.permissions import IsAdminUser,IsAuthenticated,IsAuthenticatedOrReadOnly


# Create your views here.


class create_comment(generics.CreateAPIView):
    permission_classes=[IsAuthenticatedOrReadOnly]
    queryset = comment_model.objects.all()
    serializer_class = comment_serializer
    
    
class list_comment(generics.ListAPIView):
    permission_classes=[IsAuthenticatedOrReadOnly]
    queryset = comment_model.objects.all()
    serializer_class = comment_serializer
    
class update_comment(generics.UpdateAPIView):
    permission_classes=[IsAuthenticatedOrReadOnly]
    queryset = comment_model.objects.all()
    serializer_class = comment_serializer
    
class delete_comment(generics.DestroyAPIView):
    permission_classes=[IsAuthenticatedOrReadOnly]
    queryset = comment_model.objects.all()
    serializer_class = comment_serializer