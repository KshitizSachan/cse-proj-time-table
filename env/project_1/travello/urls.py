from audioop import add
from django.urls import path
from . import views

urlpatterns = [
    path('',views.ind,name='Home_Page'),
    path('1',views.ind,name='Home_Page'),
    path('2',views.about,name='About'),
    path('3',views.add,name='Get_started'),
    path('4',views.student,name='Students time table'),
    path('5',views.faculty,name='facultys timetable'),
    path('6',views.contact,name='contact'),
    path('log',views.log,name='login'),
    path('endf',views.faculty,name='facultytime'),
    path('get',views.get,name='home'),
    path('end',views.student,name='ending')
]
