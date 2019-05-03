from django.shortcuts import render,get_object_or_404
from .models import Task
import datetime

def index(request):
    # 获取当前{week}的tasks，然后展示
    current_week = datetime.datetime.now().isocalendar()[1]
    
    # 警告! 这里的todo逻辑有问题，暂时不修改
    this_week_tasks = Task.objects.filter(date__week=current_week)
    this_week_tasks_done = this_week_tasks.filter(task_type__exact='d')
    this_week_tasks_todo = this_week_tasks.filter(task_type__exact='t')
    context = {
        'this_week_tasks_done':this_week_tasks_done,
        'this_week_tasks_todo':this_week_tasks_todo,
    }
    print(this_week_tasks[0])
    return render(request,'tasklog/index.html',context)

def detail(request,pk):
    #获取某个task的detail信息

    # try:
    #     task=Task.objects.get(pk=pk)
    # except Task.DoesNotExist:
    #     raise Http404('没有指定task!')
    # return render(request,'tasklog/detail.html',{'task':task})

    # ─── EASIER WAY ─────────────────────────────────────────────────────────────────

    task = get_object_or_404(Task,pk=pk)
    return render(request,'tasklog/detail.html',{'task':task})
    # ────────────────────────────────────────────────────────────────────────────────



def addTask(request):
    pass

def changeTask(request):
    # 修改todo为done
    pass