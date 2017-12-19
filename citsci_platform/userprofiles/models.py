from django.db import models
from django.conf import settings
import uuid

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)

    mobile_phone = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.user.username


class NHSStaffProfile(models.Model):
    nhs_profile_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    nhs_id = models.CharField(max_length=20)
    nhs_email = models.CharField(max_length=50)
    role = models.CharField(max_length=20)
    from_date = models.DateField(verbose_name='From date')
    to_date = models.DateField(verbose_name='Until Date')

    def __str__(self):
        return self.user.username