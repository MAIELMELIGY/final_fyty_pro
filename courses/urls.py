from django.urls import path
from . import views
app_name='courses'
urlpatterns = [
    path('', views.course,name='course'), 
    path('course/<int:cate_id>/',views.all_course,name='all_course')


]