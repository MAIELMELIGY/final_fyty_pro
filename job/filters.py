import django_filters
from .models import Job


 
class jobFilter(django_filters.FilterSet):
 	class Meta:
         model = Job
         fields = ['address_city','category' , "JOB_type" ]
