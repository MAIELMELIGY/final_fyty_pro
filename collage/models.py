from django.db import models
from django.contrib.auth.models import User
# Create your models here.


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
    created_dt = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.post_message
    
class comment (models.Model):
    comment=models.TextField(max_length=4000)
    posts=models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    created_by = models.ForeignKey(User,related_name='comments',on_delete=models.CASCADE)


    def __str__(self):
        return self.comment
    
    


    

