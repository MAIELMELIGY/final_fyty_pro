from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.utils.text import Truncator

class collage(models.Model):
    name = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.name

class dep(models.Model):
    dep_name = models.CharField(max_length=255)
    collage = models.ForeignKey(collage,related_name='topics',on_delete=models.CASCADE)


    def __str__(self):
        return self.dep_name
    
    
class Post(models.Model):
    post_message = models.TextField(max_length=4000)
    dep = models.ForeignKey(dep,related_name='posts',on_delete=models.CASCADE)
    #image_or_video = 
    created_by = models.ForeignKey(User,related_name='posts',on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)
    
    def __str__(self):
        truncted_message = Truncator(self.post_message)
        return truncted_message.chars(30)
    
class comment (models.Model):
    comment=models.TextField(max_length=4000)
    posts=models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    created_by = models.ForeignKey(User,related_name='comments',on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        truncted_message = Truncator(self.comment)
        return truncted_message.chars(30)
    
    
    


    

