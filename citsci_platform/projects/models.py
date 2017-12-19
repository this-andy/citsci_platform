from django.db import models
from django.conf import settings
import uuid

# Create your models here.
class Project(models.Model):
    project_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    short_name = models.CharField(max_length=20)

    def __str__(self):
        return self.short_name


class TaskType(models.Model):
    task_type_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    short_name = models.CharField(max_length=20)

    def __str__(self):
        return self.short_name


class Task(models.Model):
    task_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project = models.ForeignKey(Project)
    task_type = models.ForeignKey(TaskType)
    description = models.CharField(max_length=500, default='')

    @property
    def short_name(self):
        if self.description == '':
            display_name =  '-'.join([self.project.short_name, self.task_type.short_name])
        else:
            display_name = self.description
        return display_name

    def __str__(self):
        return self.short_name


class UserTask(models.Model):
    user_task_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    task = models.ForeignKey(Task)

    @property
    def short_name(self):
        return '-'.join([self.user.name,self.task.short_name])

    def __str__(self):
        return self.short_name
