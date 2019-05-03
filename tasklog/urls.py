from django.urls import path

from . import views

app_name='tasklog'
urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('<int:pk>',views.DetailView.as_view(),name='detail'),
    # path('addtask/',views.addTask,name='addtask'),
]