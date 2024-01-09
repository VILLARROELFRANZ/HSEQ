from django.urls import path
from . import views

urlpatterns = [
    path('', views.signin, name='signin'),
    path('home/', views.home, name='home'),
    path('signout/', views.signout, name='signout'),
    path('register_request/', views.register_request, name='register_request'),

]
