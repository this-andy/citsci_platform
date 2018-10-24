import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'citsci_platform.config.settings.local')

import django
django.setup()

from citsci_platform.projects.models import Project, TaskType, ProjectTask, User, UserProject, UserTask, UserExternalAccount, ExternalSystem

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
    {'desc': 'Systematic review for ambulance bag', 'project_id': 1, 'task_type_id':0},
    {'desc': 'Photos of ambulance equipment', 'project_id': 1, 'task_type_id': 2},
]

users = [
    {'title': 'Mr', 'first': 'Sid', 'last': 'Stransky', 'email': 'sid@email.addr'},
    {'title': 'Ms', 'first': 'Joanne', 'last': 'Julio', 'email': 'joanne@email.addr'},
    {'title': 'Mrs', 'first': 'Altha', 'last': 'Alcorn', 'email': 'altha@email.addr'},
    {'title': 'Mr', 'first': 'Darell', 'last': 'Denney', 'email': 'darell@email.addr'},
]

userprojects = [
    {'project_id': 0, 'user_id': 0},
    {'project_id': 0, 'user_id': 1},
    {'project_id': 0, 'user_id': 2},
    {'project_id': 1, 'user_id': 0},
    {'project_id': 1, 'user_id': 2},
]

usertasks =[
    {'user_project_id': 0, 'project_task_id': 0},
    {'user_project_id': 1, 'project_task_id': 1},
    {'user_project_id': 2, 'project_task_id': 0},
    {'user_project_id': 3, 'project_task_id': 2},
    {'user_project_id': 0, 'project_task_id': 1},
]

externalsystems = [
    {'name': 'Cochrane', 'short_name': 'CC', 'external_user_id_type': 'string'},
]

userexternalaccounts = [
    {'user_id': 0, 'external_system_id': 0, 'external_user_id': 'cc_user_00'},
    {'user_id': 2, 'external_system_id': 0, 'external_user_id': 'cc_user_02'},
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
        result = ProjectTask.objects.get_or_create(description=data['desc'],
                                                project_id=project_ids[data['project_id']],
                                                task_type_id=tasktype_ids[data['task_type_id']],
                                                )
        obj = result[0]
        obj.save()
        ids.append(obj.id)

    return ids


def populate_users():
    ids = []
    for data in users:
        result = User.objects.get_or_create(
            title=data['title'],
            first_name=data['first'],
            last_name=data['last'],
            email=data['email'],
        )
        obj = result[0]
        obj.save()
        ids.append(obj.id)

    return ids


def populate_user_projects(user_ids, project_ids):
    ids = []
    for data in userprojects:
        result = UserProject.objects.get_or_create(
            project_id=project_ids[data['project_id']],
            user_id=user_ids[data['user_id']],
            )
        obj = result[0]
        obj.save()
        ids.append(obj.id)

    return ids


def populate_user_tasks(userproject_ids, projecttask_ids):
    ids = []
    for data in usertasks:
        result = UserTask.objects.get_or_create(
            user_project_id = userproject_ids[data['user_project_id']],
            project_task_id=projecttask_ids[data['project_task_id']],
            )
        obj = result[0]
        obj.save()
        ids.append(obj.id)

    return ids


def populate_externalsystems():
    ids = []
    for data in externalsystems:
        result = ExternalSystem.objects.get_or_create(
            name=data['name'],
            short_name=data['short_name'],
            external_user_id_type=data['external_user_id_type']
        )
        obj = result[0]
        obj.save()
        ids.append(obj.id)

    return ids


def populate_userexternalaccounts(user_ids, externalsystem_ids):
    ids = []
    for data in userexternalaccounts:
        result = UserExternalAccount.objects.get_or_create(
            user_id = user_ids[data['user_id']],
            external_system_id=externalsystem_ids[data['external_system_id']],
            external_user_id = data['external_user_id'],
            )
        obj = result[0]
        obj.save()
        ids.append(obj.id)

    return ids

if __name__ =='__main__':
    project_ids = populate_projects()
    tasktype_ids = populate_tasktypes()
    user_ids = populate_users()
    projecttask_ids = populate_project_tasks(project_ids, tasktype_ids)
    userproject_ids = populate_user_projects(user_ids, project_ids)
    usertask_ids = populate_user_tasks(userproject_ids, projecttask_ids)
    externalsystem_ids = populate_externalsystems()
    userexternalaccount_ids = populate_userexternalaccounts(user_ids, externalsystem_ids)
