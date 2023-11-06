from django.urls import path,include
from .views import Home,Signup,Login

urlpatterns = [
    path('',Home,name='home'),
    path('home/',Home,name='homes'),
    path('signup/',Signup,name='signup'),
    path('account/',include('django.contrib.auth.urls')),
    ]

