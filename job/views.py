from django.http import HttpResponse
from . import models
from django.shortcuts import redirect, render
from .models import Job
from django.core.paginator import Paginator
from .form import ApplyForm,JobForm
from django.urls import reverse
# Create your views here.

# Create your views here.

def choice(request):
    return render(request,'Requests_send.html')




def job_list(request):
    job_list = Job.objects.all()

    paginator = Paginator(job_list, 15) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'jobs' :page_obj } # template name
    return render(request,'job_list.html',context)



def job_detail(request , slug):
    job_detail = Job.objects.get(slug=slug)

    if request.method=='POST':
        form = ApplyForm(request.POST , request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.job = job_detail
            myform.save()
            return redirect('/home/')

    else:
        form = ApplyForm()


    context = {'job' : job_detail , 'form1':form}
    return render(request,'job_details.html',context)



def add_job(request):
    if request.method=='POST':
        form = JobForm(request.POST , request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user
            myform.save()
            return redirect(reverse('jobs:job_list'))

    else:
        form = JobForm()

    return render(request,'job_upload.html',{'form':form})


        
