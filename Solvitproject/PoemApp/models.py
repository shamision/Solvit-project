from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User=get_user_model()

# class Genre(models.Model):
#     title = models.CharField(max_length=100)
    
#     def __str__(self):
#         return self.title

class Poem(models.Model):
    
    GENRES=(
        ('FAMILY','family'),
        ('LOVE','love'),
        ('SADNESS','sadness'),
        ('FRIENDSHIP','friendship'),
        ('RELATIONSHIP','relationship'),
        ('JOY','joy'),
    )
    
    FORMS=(
        ('GHAZAL','Ghazal'),
        ('HAIKU','haiku'),
        ('ITALIAN SONNET','Italian Sonnet'),
        ('LIMERICK','Limerick'),
        ('SESTINA','sestina'),
        ('TANKA','Tanka'),
        ('ELIZABETHAN SONNET','Elizabethan Sonnet'),
        ('CONTEMPORARY SONNET','Contemporary Sonnet'),
        ('VILLANELLE','Villanelle'),
        ('FREE VERSE','Free Verse'),
    )
    
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    about_poem=models.CharField(max_length=300)
    content = models.TextField()
    genre = models.CharField(max_length=20,choices=GENRES,default=GENRES[0][0])
    form = models.CharField(max_length=20,choices=FORMS,default=FORMS[0][0])
    created_on = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    