from django import template
from django.core.exceptions import ObjectDoesNotExist
from citsci_platform.userprofiles.models import UserProfile, NHSStaffProfile

register = template.Library()


@register.inclusion_tag('userprofiles/userprofilelist.html')
def get_userprofile(user_fk):
    print('get_userprofile invoked')

    try:
        profile = UserProfile.objects.get(user_id=user_fk)
        return {'profile': {'mobile' : profile.mobile_phone}}
    except ObjectDoesNotExist:
        return {}


@register.inclusion_tag('userprofiles/nhsprofilelist.html')
def get_nhsprofile(user_fk):
    try:
        profile = NHSStaffProfile.objects.get(user_id=user_fk)
        return {'profile': {'nhs_id' : profile.nhs_id, 'nhs_email' : profile.nhs_email}}
    except ObjectDoesNotExist:
        return {}

# print('get_userprofile loaded')
