from django.urls import path
from . import views

urlpatterns = [
    #Views
    path('', views.LoginView, name='login_view'),
    path('dashboard', views.DashboardView, name='dashboard_view'),

    #Process
    path('login-process', views.LoginProcess, name='login_process'),
    path('logout-process', views.LogoutProcess, name='logout_process')

]