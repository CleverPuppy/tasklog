from django.forms import ModelForm
from .models import Task

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'



# from django import forms

# class TaskForm(forms.Form):
#     title = forms.CharField(label='title',max_length=200)
#     content = forms.Textarea()
