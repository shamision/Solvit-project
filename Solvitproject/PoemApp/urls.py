from django.urls import path
from .views import *

urlpatterns = [
    path('createPoem', createPoem.as_view()),
    path('viewPoem', viewPoem.as_view()),
    path('editPoem/<int:pk>/', editPoem.as_view()),
    path('deletePoem/<int:pk>/', deletePoem.as_view()),
]
