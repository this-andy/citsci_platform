from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)

    mobile_phone = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.user.username


class NHSStaffProfile(models.Model):
    user = models.ForeignKey(User)

    nhs_id = models.CharField(max_length=20)
    role = models.CharField(max_length=20)
    from_date = models.DateField(verbose_name='From date')
    to_date = models.DateField(verbose_name='Until Date')

    def __str__(self):
        return self.user.username
