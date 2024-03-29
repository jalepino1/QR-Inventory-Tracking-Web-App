
from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('scanner/', views.scanner, name='scanner'),
    path('robotics_lab/', views.robotics_lab, name='robotics_lab'),
    path('vr_lab/', views.vr_lab, name='vr_lab'),
    path('robotics_lab/alienware/', views.alienware, name='alienware'),
    path('robotics_lab/sparkfun/', views.sparkfun, name='sparkfun'),
    path('robotics_lab/teacherpack/', views.teacherpack, name='teacherpack'),
    path('robotics_lab/spheros/', views.spheros, name='spheros'),
    path('robotics_lab/raspberry_pi/', views.raspberry_pi, name='raspberry_pi'),
    path('robotics_lab/alienware/add_alienware/', views.add_alienware, name='add_alienware'),
    path('robotics_lab/sparkfun/add_sparkfun/', views.add_sparkfun, name='add_sparkfun'),
    path('robotics_lab/teacherpack/add_teacherpack/', views.add_teacherpack, name="add_teacherpack"),
    path('robotics_lab/raspberry_pi/add_raspberry_pi/', views.add_raspberry_pi, name='add_raspberry_pi'),
    
]
