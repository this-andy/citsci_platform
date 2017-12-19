from django.contrib import admin

from .models import Project, TaskType, Task, UserTask

# Register your models here.

admin.site.register(Project)
admin.site.register(TaskType)
admin.site.register(Task)
admin.site.register(UserTask)
