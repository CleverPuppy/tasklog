from django import forms

class TaskForm(forms.Form):
    title = forms.CharField(label='title',max_length=200)
    content = forms.Textarea()
