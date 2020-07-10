from django.urls import include, path
from django.contrib.auth import views as auth_views
from . import views

app_name='accounts'

urlpatterns = [
    path('signup/',views.signup , name='signup'),
    path('profile',views.profile , name='profile'),
    path('profile/edit',views.profile_edit , name='profile_edit'),
    path('login/',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout')
]