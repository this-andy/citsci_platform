from django.db import models
from django.conf import settings
import uuid

from ..models import TimeStampedModel

# Create your models here.
class UserProfile(TimeStampedModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    nhs_staff = models.NullBooleanField(default=None)
    mobile_phone = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.user.username


class NHSStaffProfile(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    nhs_id = models.CharField(max_length=20)
    nhs_email = models.CharField(max_length=50)
    role = models.CharField(max_length=20)
    from_date = models.DateField(verbose_name='From date')
    to_date = models.DateField(verbose_name='Until Date')

    def __str__(self):
        return self.user.username
