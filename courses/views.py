from django.shortcuts import render, get_object_or_404,redirect
from django.shortcuts import redirect, render
from django.http import HttpResponse,Http404
from .models import cate ,ALL_COURSE
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.urls import reverse

# Create your views here.

def course(request):
    courses = cate.objects.all()
    return render(request,'course_cat.html',{'courses':courses})


def all_course(request,cate_id):
    # try:
    #     board = Board.objects.get(pk=board_id)
    # except Board.DoesNotExist:
    #     raise Http404
    boards = get_object_or_404(cate ,pk= cate_id)
    return render(request,'x.html',{'boards':boards})



    