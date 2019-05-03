from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import generic

import datetime

from .models import Task

class IndexView(generic.ListView):
    template_name = 'tasklog/index.html'
    current_week = datetime.datetime.today().isocalendar()[1]
    queryset = Task.objects.filter(date__week = current_week)
    def get_context_data(self,**kwargs):
        context = super(IndexView,self).get_context_data(**kwargs)
        context['this_week_tasks_done'] = self.queryset.filter(task_type__exact='d')
        context['this_week_tasks_todo'] = self.queryset.filter(task_type__exact='t')
        return context


class DetailView(generic.DeleteView):
    model = Task
    object_name='task'
    template_name = 'tasklog/detail.html'





















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