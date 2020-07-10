
from django.urls import path
from . import views
app_name='travel'
urlpatterns = [
    path('',views.trip_list,name='trips')
]