from django.urls import path
from .views import *

urlpatterns = [
    path('createComment', create_comment.as_view()),
    path('listComment', list_comment.as_view()),
    path('updateComment/<int:pk>/', update_comment.as_view()),
    path('deleteComment/<int:pk>/', delete_comment.as_view()),
]