from django.urls import path
from . import views

urlpatterns = [
    path('calc',views.calc, name='calc'),
    path('',views.home, name='home'),
    path('add',views.add, name='add'),
    path('sub',views.sub, name='sub'),
    path('mul',views.mul, name='mul'),
    path('div',views.div, name='div'),
    path('choice',views.options, name='options'),
    path('register',views.registerpage, name='registerpage'),
    path('login',views.loginpage, name='loginpage'),
     path('logout',views.logout, name='logout'),
]