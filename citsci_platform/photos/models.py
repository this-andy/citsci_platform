from django.conf import settings
from django.db import models
from django.template.defaultfilters import slugify
from PIL import Image
from .exif_pil import get_clean_gps_info_from_image
from ..models import TimeStampedModel
from ..users.models import User

# Create your models here.

class Photo(TimeStampedModel):
    name = models.CharField(max_length=100)
    taken_on = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    location_name = models.CharField(max_length=255, null=True, blank=True)
    # taken_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="picture_taken_by", null=True, blank=True)
    taken_by = models.IntegerField(null=True, blank=True)
    file_location = models.CharField(max_length=1000, null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)
    image = models.ImageField(upload_to='uploads', blank=True, null=True)


    @property
    def taken_by_name(self):
        if self.taken_by == None:
            return 'Unknown'
        else:
            user = User.objects.get(id=self.taken_by)
            return user.name


    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.name)
        super(Photo, self).save(force_insert, force_update, using, update_fields)


    def __str__(self):
        return '{0}, {1}, {2}'.format(self.name, self.location_name, self.date_created)


    def extract_image_info(self):
        if self.file_location:
            image = Image.open(self.file_location)
            exif_info = get_clean_gps_info_from_image(image)
            self.latitude = exif_info['Latitude']
            self.longitude = exif_info['Longitude']
            self.date_created = exif_info['TimeStamp']
            self.save()
