from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.utils.text import slugify

class cate(models.Model):
    cat_name = models.CharField(max_length=50,unique=True)
    image = models.ImageField( upload_to='images/' ,null=True)
   
    def __str__(self):
        return self.cat_name



class ALL_COURSE(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    link = models.CharField(max_length=100)
    instructor = models.CharField( max_length=50)
    #created_by = models.ForeignKey(User,related_name='posts',on_delete=models.CASCADE, null=True)
    created_dt = models.DateTimeField(auto_now_add=True , null=True)
    cate= models.ForeignKey(cate,on_delete=models.CASCADE,related_name='courses')

    def __str__(self):
        return self.name 


