
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.

from django.db import models

from django.utils.text import slugify

from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
# Create your models here.
# Create your models here.

JOB_TYPE= (
('Full time','Full time'),
('Freelancer','Freelancer'),
('Part-time','Part time'),
('Internship','Internship '),
)
CAREER_CHOICES=(
    ('student','student'),
    ('Entry Level','Entry Level'),
    ('Experienced','Experienced'),
    ('manager','manager'),
    ('Senior Management','Senior Management')
)



def image_upload(instance,filename):
    imagename, extension = filename.split(".")
    return "jobs/%s.%s"%(instance.id,extension)


class Job(models.Model):
    owner = models.ForeignKey(User, related_name='job_owner', on_delete=models.CASCADE)
    Vacancy = models.IntegerField(default=1)
    company_name=models.CharField( _("اسم الشركه :"),max_length=50,null=True)
    job_name=models.CharField(_("اسم الوظيفه"), max_length=254,null=True)
    address_country= models.CharField(_("الدوله "), max_length=50,null=True)
    address_city = models.CharField(_("المدينه"), max_length=50 , null=True)
    address_area = models.CharField(_("المنطقه"), max_length=50 ,null=True)
    description = models.TextField(max_length=1000)
    Job_Requirements = models.TextField(_("متطلبات الوظيفه") ,null=True)
    Career_Level = models.CharField(_("مستوى الخبره"),choices=CAREER_CHOICES, max_length=30 , null=True)
    Email = models.EmailField(_("البريد الالكترونى للشركه"), max_length=254 ,null=True)
    JOB_type = models.CharField(_("نوع الشغل"),choices=JOB_TYPE,default='FULL TIME',max_length=30,null=True)
    available = models.BooleanField(_("متاح") ,null=True)
    Company_details = models.TextField(_("معلومات عن الشركه "), null=True)
    Created = models.DateTimeField(_(" وقت نشر الوظيفه"), auto_now_add=True,null=True)
    update = models.DateTimeField(_("وقت تعديل الوظيفه"), auto_now=True ,null=True)
    slug = models.SlugField(_("slug"),blank=True, null=True)
    salary = models.IntegerField(_("المرتب") ,default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    image = models.ImageField(_("صوره"),upload_to=image_upload)


    def save(self, *args, **kwargs):
       if not self.slug:
           self.slug= slugify(self.job_name)
       super(Job, self).save(*args, **kwargs) # Call the real save() method
    def __str__(self):
        return self.job_name


class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name




class Apply(models.Model):
    job = models.ForeignKey(Job, related_name='apply_job', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    webiste = models.URLField()
    cv = models.FileField(upload_to='apply/')
    cover_letter = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name