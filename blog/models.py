from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse #

# Create your models here.
class Post(models.Model):
    title = models.TextField(max_length=100)
    cover = models.ImageField(upload_to='images/')
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    def __str__(self):
        return self.title
    
    def get_absolute_url(self): # new
        return reverse('post_detail', args=[str(self.id)])

    
    

