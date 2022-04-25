from django.urls import path
from . import views

urlpatterns = [
    #Views
    path('', views.LoginView, name='login-view'),

    #Process
    path('login-process', views.LoginProcess, name='login-process'),
    path('logout-process', views.LogoutProcess, name='logout-process')

]