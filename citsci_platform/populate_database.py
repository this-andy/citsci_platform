import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'citsci_platform.config.settings.local')

import django
django.setup()

from citsci_platform.projects.models import Project, TaskType, Task, UserTask

def populate_projects():
    proj1 = Project.objects.get_or_create(name='CTG Monitoring', short_name='CTG Monitoring')
    proj1[0].save()
    proj2 = Project.objects.get_or_create(name='Ambulance equipment', short_name='Ambulance equipment')
    proj2[0].save()
    return [proj1[0].project_id, proj2[0].project_id]


def populate_tasktypes():
    tt1 = TaskType.objects.get_or_create(name='Systematic review', short_name='Systematic review')
    tt1[0].save()
    tt2 = TaskType.objects.get_or_create(name='Skills assessment', short_name='Skills assessment')
    tt2[0].save()
    tt3 = TaskType.objects.get_or_create(name='Photo upload', short_name='Photo upload')
    tt3[0].save()
    return [tt1[0].task_type_id, tt2[0].task_type_id, tt3[0].task_type_id]

def populate_project_tasks(project_ids, tasktype_ids):
    desc = 'Systematic review for CTG monitoring'
    pt = Task.objects.get_or_create(project_id=project_ids[0], task_type_id=tasktype_ids[0], description=desc)
    pt[0].save()
    desc = 'Midwife assessment for CTG monitoring'
    pt = Task.objects.get_or_create(project_id=project_ids[0], task_type_id=tasktype_ids[1], description=desc)
    pt[0].save()
    desc = 'Photos of ambulance equipment'
    pt = Task.objects.get_or_create(project_id=project_ids[1], task_type_id=tasktype_ids[2], description=desc)
    pt[0].save()

if __name__ =='__main__':
    project_ids = populate_projects()
    tasktype_ids = populate_tasktypes()
    populate_project_tasks(project_ids, tasktype_ids)
