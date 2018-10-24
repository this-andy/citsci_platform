from django.db import models

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


class User(TimeStampedModel):
    email = models.CharField(max_length=100, blank=True, null=True)
    email_address_verified = models.BooleanField(default=False)
    title = models.CharField(max_length=20, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    auth0_id = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=12, blank=True, null=True)

    def __str__(self):
        return self.email

    @property
    def full_name(self):
        return str(self.first_name) + ' ' + str(self.last_name)


class Project(TimeStampedModel):
    STATUS_CHOICES = (
        ('planned', 'Planned'),
        ('active', 'Active'),
        ('complete', 'Complete')
    )
    name = models.CharField(max_length=50)
    short_name = models.CharField(max_length=20, blank=True)
    status = models.CharField(max_length=12, blank=True, null=True, choices=STATUS_CHOICES)

    def __str__(self):
        return get_display_name(self) + ' (' + str(self.status) + ')'


class TaskType(TimeStampedModel):
    name = models.CharField(max_length=50)
    short_name = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return get_display_name(self)


class ProjectTask(TimeStampedModel):
    STATUS_CHOICES = (
        ('planned', 'Planned'),
        ('active', 'Active'),
        ('complete', 'Complete')
    )
    SIGNUP_STATUS_CHOICES = (
        ('not-open', 'Not yet open'),
        ('open', 'Open'),
        ('invitation', 'Invitation only'),
        ('closed', 'Closed')
    )
    project = models.ForeignKey(Project)
    task_type = models.ForeignKey(TaskType)
    description = models.CharField(max_length=500, default='')
    earliest_start_date = models.DateTimeField(null=True, blank=True)
    closing_date = models.DateTimeField(null=True, blank=True)
    signup_status = models.CharField(max_length=12, blank=True, null=True, choices=SIGNUP_STATUS_CHOICES)
    status = models.CharField(max_length=12, blank=True, null=True, choices=STATUS_CHOICES)

    @property
    def short_name(self):
        if self.description == '':
            display_name = '-'.join([self.project.short_name, self.task_type.short_name])
        else:
            display_name = self.description
        return display_name

    def __str__(self):
        return self.short_name + ' (' + str(self.status) + ')'


class UserProject(TimeStampedModel):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL)
    user = models.ForeignKey(User)
    project = models.ForeignKey(Project)
    status = models.CharField(max_length=12, blank=True, null=True)

    @property
    def short_name(self):
        return '-'.join([self.user.full_name, self.project.short_name])

    def __str__(self):
        return self.short_name


class UserTask(TimeStampedModel):
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('complete', 'Complete')
    )
    # user = models.ForeignKey(settings.AUTH_USER_MODEL)
    user_project = models.ForeignKey(UserProject)
    # task = models.ForeignKey(Task)
    project_task = models.ForeignKey(ProjectTask)
    status = models.CharField(max_length=12, blank=True, null=True, choices=STATUS_CHOICES)
    consented = models.DateTimeField(null=True)

    @property
    def short_name(self):
        return '-'.join([self.user_project.short_name, self.project_task.short_name])

    def __str__(self):
        return self.short_name


class ExternalSystem(TimeStampedModel):
    name = models.CharField(max_length=50)
    short_name = models.CharField(max_length=20, blank=True)
    external_user_id_type = models.CharField(max_length=10, blank=True, null=True)  # uuid, integer, string

    def __str__(self):
        return get_display_name(self)


class UserExternalAccount(TimeStampedModel):
    external_system = models.ForeignKey(ExternalSystem)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL)
    user = models.ForeignKey(User)
    external_user_id = models.CharField(max_length=50)
    status = models.CharField(max_length=12, blank=True, null=True)

    @property
    def short_name(self):
        return '-'.join([self.external_system.short_name, self.user.full_name])

    def __str__(self):
        return self.short_name


class EntityUpdate(TimeStampedModel):
    entity_name = models.CharField(max_length=50)
    entity_id = models.UUIDField(editable=False)
    json_patch = models.CharField(max_length=2000, editable=False)
    json_reverse_patch = models.CharField(max_length=2000, editable=False)


class UserGroup(TimeStampedModel):
    name = models.CharField(max_length=50)
    short_name = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return get_display_name(self)


class UserGroupMembership(TimeStampedModel):
    user = models.ForeignKey(User)
    user_group = models.ForeignKey(UserGroup)

    @property
    def short_name(self):
        return '-'.join([self.user.full_name, self.user_group.short_name])

    def __str__(self):
        return self.short_name


class ProjectGroupVisibility(TimeStampedModel):
    project = models.ForeignKey(Project)
    user_group = models.ForeignKey(UserGroup)

    @property
    def short_name(self):
        return '-'.join([self.project.short_name, self.user_group.short_name])

    def __str__(self):
        return self.short_name


class ProjectTaskGroupVisibility(TimeStampedModel):
    project_task = models.ForeignKey(ProjectTask)
    user_group = models.ForeignKey(UserGroup)

    @property
    def short_name(self):
        return '-'.join([self.project_task.short_name, self.user_group.short_name])

    def __str__(self):
        return self.short_name
