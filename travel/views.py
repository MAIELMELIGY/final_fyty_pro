from django.http import HttpResponse
from . import models
from django.shortcuts import redirect, render
from .models import travel
from django.core.paginator import Paginator
from django.urls import reverse
# Create your views here.

# Create your views here.




def trip_list(request):
    travels =travel.objects.all()

    paginator = Paginator(travels, 10) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'trips' :page_obj } # template name
    return render(request,'travel.html',context)


