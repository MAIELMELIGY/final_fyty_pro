
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.

from django.db import models

from django.utils.text import slugify

from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class travel(models.Model):

    place= models.CharField(_("المكان"), max_length=50)
    price = models.IntegerField(_("السعر"))
    date=models.DateField(_("معاد الرحله"), auto_now=False, auto_now_add=False)
    time=models.TimeField(_("معاد الصعود"), auto_now=False, auto_now_add=False)
    days_lenght=models.IntegerField(_("مده الرحله "))



    def __str__(self):
        return self.place