from django.db import models
from django.conf import settings

from ..models import TimeStampedModel


def get_display_name(self):
    short_name_length = self.__class__._meta.get_field('short_name').max_length
    if self.short_name == '':
        if len(self.name) > short_name_length:
            return self.name[:short_name_length - 2] + '...'
        else:
            return self.name
    else:
        return self.short_name


# Create your models here.
class Project(TimeStampedModel):
    name = models.CharField(max_length=50)
    short_name = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return get_display_name(self)



class TaskType(TimeStampedModel):
    name = models.CharField(max_length=50)
    short_name = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return get_display_name(self)


class Task(TimeStampedModel):
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


class UserProject(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    project = models.ForeignKey(Project)

    @property
    def short_name(self):
        return '-'.join([self.user.name,self.project.short_name])

    def __str__(self):
        return self.short_name


class UserTask(TimeStampedModel):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL)
    user_project = models.ForeignKey(UserProject)
    task = models.ForeignKey(Task)

    @property
    def short_name(self):
        return '-'.join([self.user_project.short_name,self.task.short_name])

    def __str__(self):
        return self.short_name
