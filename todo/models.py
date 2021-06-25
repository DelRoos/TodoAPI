from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Status(models.Model):
    name = models.CharField(max_length=30, unique=True)
    describe = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        return super(Status, self).save(*args, **kwargs)

    # def __init__(self, *args, **kwargs):
    #     self.name = self.name.lower()
    
    # def __str__(self):
    #     return self.id

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='task_user')
    title = models.CharField(max_length=50)
    body = models.TextField()
    state = models.ForeignKey(Status, on_delete=models.CASCADE, related_name='task_state')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
