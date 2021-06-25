from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Status(models.Model):
    name = models.CharField(max_length=30, unique=True)
    describe = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __init__(self, *args, **kwargs):
        self.name = self.name.lower()

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='task_user')
    title = models.CharField(max_length=50)
    body = models.TextField()
    state = models.ForeignKey(Status, on_delete=models.CASCADE, related_name='task_state')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# {
#     "user": 1,
#     "title": "laver les habit",
#     "body": "laver les vetements de mes parent et les miens"
# }