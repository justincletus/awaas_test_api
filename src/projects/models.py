from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    duration = models.IntegerField(max_length=50, default=1, blank=True)
    date = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return f"/project/{self.id}/update"

    def __str__(self):
        return self.title

class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField(default=datetime.now)
    end_date = models.DateField(default=datetime.now)
    date = models.DateTimeField(default=timezone.now)
    
    def get_absolute_url(self):
        return f"/task/{self.id}/update"
    
    def __str__(self):
        return self.title
