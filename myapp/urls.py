from django.urls import path
from . import views

urlpatterns = [path('index', views.index, name = 'index'),
               path('register', views.register,name= 'register'),
               path('login', views.login, name='login'),
               path('', views.register_now, name='register_now'),
               path('logout', views.logout, name='logout'),
               path('example_link', views.example_links, name='example_link'),
               path('post/<str:abc>', views.post, name='post'),
               ]