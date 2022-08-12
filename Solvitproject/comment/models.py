from django.db import models
from PoemApp.models import Poem

# Create your models here.

class comment_model(models.Model):
    content = models.CharField(max_length=100)
    poem = models.ForeignKey(Poem, on_delete=models.CASCADE)
    created_on = models.DateField(auto_now_add=True)