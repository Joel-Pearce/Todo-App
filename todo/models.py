from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    task_title = models.CharField(max_length=100)
    task_description = models.TextField(blank=True)
    date_set = models.DateTimeField(auto_now_add=True)
    date_due = models.DateTimeField(null=True, blank=True)
    importance = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.task_title

