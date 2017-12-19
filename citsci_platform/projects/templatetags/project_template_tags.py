from django import template
from django.core.exceptions import ObjectDoesNotExist
from citsci_platform.projects.models import Project, UserTask, Task, TaskType

register = template.Library()


@register.inclusion_tag('projects/usertasklist.html')
def get_userprojects(user_fk):
    print('get_userprojects invoked')

    try:
        profile = UserTask.objects.filter(user_id=user_fk)
        # print(profile)
        return {'usertasks': profile}
    except ObjectDoesNotExist:
        return {}


# print('get_userprojects loaded')
