from django.db import models

# Create your models here.
class Task(models.Model):
    task_type_choices = (
        ('d','done'),
        ('t','todo'),
    )
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    date=models.DateTimeField('date added',auto_now_add=True)
    done_date=models.DateTimeField('date done',auto_now=True)
    task_type = models.TextField(choices=task_type_choices)

    def __str__(self):
        return self.title
