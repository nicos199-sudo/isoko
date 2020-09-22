from django.urls import path
from . import views



urlpatterns = [
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('', views.Dashboard, name='home'),

    path('logout/', views.Logout, name='logout'),
    path('login/', views.LoginView.as_view(), name='login'),
]
