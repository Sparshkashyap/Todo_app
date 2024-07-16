from django.urls import path

from . import views

urlpatterns=[
    path("",views.home,name='home'),
    path("todo/",views.todo,name='todo'),
    path("add_todo/",views.add_todo,name='add')
]