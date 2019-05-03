from django.urls import path

from . import views

app_name='tasklog'
urlpatterns = [
    path('',views.index,name='index'),
    path('<int:pk>',views.detail,name='detail'),
    path('addtask/',views.addTask,name='addtask'),
]