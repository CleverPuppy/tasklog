# _*_ coding: utf-8 _*_
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404,render
from django.urls import reverse
from django.views import generic
from django.core.mail import send_mail
from django.conf import settings
from email.header import Header
import datetime

from .models import Task
from .forms import TaskForm

class IndexView(generic.ListView):
    template_name = 'tasklog/index.html'
    current_week = datetime.date.today().isocalendar()[1]
    queryset = Task.objects.filter(date__week = current_week, task_type__exact='d')
    def get_context_data(self,**kwargs):
        context = super(IndexView,self).get_context_data(**kwargs)
        context['this_week_tasks_done'] = self.queryset
        context['this_week_tasks_todo'] = Task.objects.filter(task_type__exact='t').order_by('date')
        return context


class DetailView(generic.DeleteView):
    model = Task
    object_name='task'
    template_name = 'tasklog/detail.html'

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            # add to datebase
            form.save()
            return HttpResponseRedirect('/tasklog/')
    else:
        form = TaskForm()
    
    return render(request,'tasklog/addtask.html',{'form':form})

def send_email(request):
    current_week = datetime.date.today().isocalendar()[1]
    this_week_tasks_done = Task.objects.filter(date__week=current_week,task_type__exact='d')
    next_week_tasks_todo = Task.objects.filter(task_type__exact='t').order_by('date')[:2]

    message_content = "李老师，现在向您汇报本周工作和下周工作计划：\n\n本周工作：\n"
    print(type(this_week_tasks_done))
    i=0
    for task in this_week_tasks_done:
        message_content += "    "+ str(i+1) +". " + str(task.title)+"\n"
        message_content += "        "+str(task.content) +"\n"
        i+=1
    
    message_content += "\n" + "下周工作计划:\n"
    i=0
    for task in next_week_tasks_todo:
        message_content += "    "+ str(i+1) +". " + str(task.title)+"\n"
        i+=1

    message_content += "\n\n\n丁鹏辉"
    message_subject = "丁鹏辉_每周汇报_" + str(datetime.date.today())
    message_from = Header('丁鹏辉','utf-8').encode() + ' <919479850@qq.com>'
    message_to   = Header('李俊老师','utf-8').encode()+ ' <220184402@seu.edu.cn>'
    send_mail(message_subject,message_content,message_from,(message_to,))
















# ────────────────────────────────────────────────────────────────────────────────


# from django.shortcuts import render,get_object_or_404
# from .models import Task
# import datetime

# def index(request):
#     # 获取当前{week}的tasks，然后展示
#     current_week = datetime.datetime.now().isocalendar()[1]
    
#     # 警告! 这里的todo逻辑有问题，暂时不修改
#     this_week_tasks = Task.objects.filter(date__week=current_week)
#     this_week_tasks_done = this_week_tasks.filter(task_type__exact='d')
#     this_week_tasks_todo = this_week_tasks.filter(task_type__exact='t')
#     context = {
#         'this_week_tasks_done':this_week_tasks_done,
#         'this_week_tasks_todo':this_week_tasks_todo,
#     }
#     print(this_week_tasks[0])
#     return render(request,'tasklog/index.html',context)

# def detail(request,pk):
#     #获取某个task的detail信息

#     # try:
#     #     task=Task.objects.get(pk=pk)
#     # except Task.DoesNotExist:
#     #     raise Http404('没有指定task!')
#     # return render(request,'tasklog/detail.html',{'task':task})

#     # ─── EASIER WAY ─────────────────────────────────────────────────────────────────

#     task = get_object_or_404(Task,pk=pk)
#     return render(request,'tasklog/detail.html',{'task':task})
#     # ────────────────────────────────────────────────────────────────────────────────



# def addTask(request):
#     #添加TASK的VIEW
#     return render(request,'tasklog/addtask.html')

# def changeTask(request):
#     # 修改todo为done
#     pass