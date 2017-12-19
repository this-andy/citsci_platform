import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'citsci_platform.config.settings.local')

import django
django.setup()

from citsci_platform.projects.models import Project, TaskType, Task, UserTask

projects = [
    {'name': 'CTG Monitoring', 'short_name': 'CTG Monitoring'},
    {'name': 'Ambulance equipment', 'short_name': 'Ambulance equipment'},
]

tasktypes = [
    {'name': 'Systematic review', 'short_name': 'Systematic review'},
    {'name': 'Skills assessment', 'short_name': 'Skills assessment'},
    {'name': 'Photo upload', 'short_name': 'Photo upload'},
]

projecttasks =[
    {'desc': 'Systematic review for CTG monitoring', 'project_id': 0, 'task_type_id':0},
    {'desc': 'Midwife assessment for CTG monitoring', 'project_id': 0, 'task_type_id': 1},
    {'desc': 'Photos of ambulance equipment', 'project_id': 1, 'task_type_id': 2},
]

def populate_projects():
    ids = []
    for data in projects:
        result = Project.objects.get_or_create(name=data['name'], short_name=data['short_name'])
        obj = result[0]
        obj.save()
        ids.append(obj.id)

    return ids


def populate_tasktypes():
    ids = []
    for data in tasktypes:
        result = TaskType.objects.get_or_create(name=data['name'], short_name=data['short_name'])
        obj = result[0]
        obj.save()
        ids.append(obj.id)

    return ids


def populate_project_tasks(project_ids, tasktype_ids):
    ids = []
    for data in projecttasks:
        result = Task.objects.get_or_create(description=data['desc'],
                                                project_id=project_ids[data['project_id']],
                                                task_type_id=tasktype_ids[data['task_type_id']],
                                                )
        obj = result[0]
        obj.save()
        ids.append(obj.id)

    return ids


if __name__ =='__main__':
    project_ids = populate_projects()
    tasktype_ids = populate_tasktypes()
    populate_project_tasks(project_ids, tasktype_ids)
