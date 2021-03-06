from django.db import models
import uuid
from ..models import TimeStampedModel


def get_display_name(self):
    short_name_length = self.__class__._meta.get_field('short_name').max_length
    if self.short_name == '':
        if len(self.name) > short_name_length:
            return self.name[:short_name_length - 2] + '...'
        else:
            return self.name
    else:
        return self.short_name + '{' + str(self.id) + '}'


class User(TimeStampedModel):
    email = models.CharField(max_length=100, blank=True, null=True)
    email_address_verified = models.BooleanField(default=False)
    email_verification_token = models.UUIDField(default=uuid.uuid4(), null=True, editable=False)
    email_verification_expiry = models.DateTimeField(null=True, editable=False)
    title = models.CharField(max_length=20, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    auth0_id = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=12, blank=True, null=True)

    def __str__(self):
        return self.email + ' (' + self.full_name + ') {' + str(self.id) + '}'

    @property
    def full_name(self):
        return str(self.first_name) + ' ' + str(self.last_name)


class UserGroup(TimeStampedModel):
    name = models.CharField(max_length=50)
    short_name = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return get_display_name(self)


class ExternalSystem(TimeStampedModel):
    name = models.CharField(max_length=50)
    short_name = models.CharField(max_length=20, blank=True)
    external_user_id_type = models.CharField(max_length=10, blank=True, null=True)  # uuid, integer, string


    def __str__(self):
        return get_display_name(self)


class Project(TimeStampedModel):
    STATUS_CHOICES = (
        ('planned', 'Planned'),
        ('testing', 'Testing'),
        ('active', 'Active'),
        ('complete', 'Complete')
    )
    VISIBILITY_CHOICES = (
        ('public', 'Public'),
        ('private', 'Private'),
    )
    name = models.CharField(max_length=50)
    short_name = models.CharField(max_length=20, blank=True)
    visibility = models.CharField(max_length=12, choices=VISIBILITY_CHOICES)
    website_highlight = models.BooleanField(default=False)
    testing_group = models.ForeignKey(UserGroup, null=True, blank=True)
    status = models.CharField(max_length=12, choices=STATUS_CHOICES)

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
        ('testing', 'Testing'),
        ('active', 'Active'),
        ('complete', 'Complete')
    )
    SIGNUP_STATUS_CHOICES = (
        ('not-open', 'Not yet open'),
        ('open', 'Open'),
        ('closed', 'Closed')
    )
    VISIBILITY_CHOICES = (
        ('public', 'Public'),
        ('private', 'Private'),
    )
    project = models.ForeignKey(Project)
    task_type = models.ForeignKey(TaskType)
    description = models.CharField(max_length=500, default='')
    earliest_start_date = models.DateTimeField(null=True, blank=True)
    closing_date = models.DateTimeField(null=True, blank=True)
    signup_status = models.CharField(max_length=12, choices=SIGNUP_STATUS_CHOICES)
    visibility = models.CharField(max_length=12, choices=VISIBILITY_CHOICES)
    website_highlight = models.BooleanField(default=False)
    testing_group = models.ForeignKey(UserGroup, null=True, blank=True)
    external_system = models.ForeignKey(ExternalSystem, null=True, blank=True)
    external_task_id = models.CharField(max_length=50, null=True, blank=True)
    status = models.CharField(max_length=12, choices=STATUS_CHOICES)

    @property
    def short_name(self):
        if self.description == '':
            display_name = '-'.join([self.project.short_name, self.task_type.short_name])
        else:
            display_name = self.description
        return display_name

    def __str__(self):
        return self.short_name + ' (' + str(self.status) + ') {' + str(self.id) + '}'


class UserProject(TimeStampedModel):
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('complete', 'Complete'),
        ('withdrawn', 'Withdrawn')
    )
    user = models.ForeignKey(User)
    project = models.ForeignKey(Project)
    status = models.CharField(max_length=12, blank=True, null=True, choices=STATUS_CHOICES)

    @property
    def short_name(self):
        return '-'.join([self.user.full_name, self.project.short_name])

    def __str__(self):
        return self.short_name + ' {' + str(self.id) + '}'


class UserTask(TimeStampedModel):
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('complete', 'Complete'),
        ('withdrawn', 'Withdrawn')
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
        return self.short_name + ' {' + str(self.id) + '}'


class UserExternalAccount(TimeStampedModel):
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('closed', 'Closed')
    )
    external_system = models.ForeignKey(ExternalSystem)
    user = models.ForeignKey(User)
    external_user_id = models.CharField(max_length=50, null=True, blank=True, choices=STATUS_CHOICES)
    status = models.CharField(max_length=12, blank=True, null=True)

    @property
    def short_name(self):
        return '-'.join([self.external_system.short_name, self.user.full_name])

    def __str__(self):
        return self.short_name + ' {' + str(self.id) + '}'


class EntityUpdate(TimeStampedModel):
    entity_name = models.CharField(max_length=50)
    entity_id = models.UUIDField(editable=False)
    json_patch = models.CharField(max_length=2000, editable=False)
    json_reverse_patch = models.CharField(max_length=2000, editable=False)


class UserGroupMembership(TimeStampedModel):
    user = models.ForeignKey(User)
    user_group = models.ForeignKey(UserGroup)

    @property
    def short_name(self):
        return '-'.join([self.user.full_name, self.user_group.short_name])

    def __str__(self):
        return self.short_name + ' {' + str(self.id) + '}'


class ProjectGroupVisibility(TimeStampedModel):
    project = models.ForeignKey(Project)
    user_group = models.ForeignKey(UserGroup)

    @property
    def short_name(self):
        return '-'.join([self.project.short_name, self.user_group.short_name])

    def __str__(self):
        return self.short_name + ' {' + str(self.id) + '}'


class ProjectTaskGroupVisibility(TimeStampedModel):
    project_task = models.ForeignKey(ProjectTask)
    user_group = models.ForeignKey(UserGroup)

    @property
    def short_name(self):
        return '-'.join([self.project_task.short_name, self.user_group.short_name])

    def __str__(self):
        return self.short_name + ' {' + str(self.id) + '}'
