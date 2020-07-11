from django.urls import path
from . import views
app_name = "collage"
urlpatterns = [
    path('',views.collage_list,name='home'),
 
]