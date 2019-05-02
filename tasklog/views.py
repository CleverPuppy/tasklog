from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Task
import datetime

def index(request):
    # 获取当前{week}的tasks，然后展示
    current_week = datetime.datetime.now().isocalendar()[1]
    
    # 警告! 这里的todo逻辑有问题，暂时不修改
    this_week_tasks = Task.objects.filter(date__week=current_week)
    this_week_tasks_done = this_week_tasks.filter(task_type__exact='d')
    this_week_tasks_todo = this_week_tasks.filter(task_type__exact='t')
    template = loader.get_template('tasklog/index.html')
    context = {
        'this_week_tasks_done':this_week_tasks_done,
        'this_week_tasks_todo':this_week_tasks_todo,
    }
    print(this_week_tasks[0])
    return HttpResponse(template.render(context,request))

def addTask(request):
    return HttpResponse('YOU ARE ADDING A TASK!')

def changeTask(request):
    # 修改todo为done
    pass