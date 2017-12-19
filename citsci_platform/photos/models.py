from django.conf import settings
from django.db import models
from django.template.defaultfilters import slugify
from PIL import Image
from citsci_platform.photos.exif_pil import get_clean_gps_info_from_image

# Create your models here.

class Photo(models.Model):
    name = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    location_name = models.CharField(max_length=255, null=True)
    taken_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="picture_taken_by", null=True)
    file_location = models.CharField(max_length=1000, null=True)
    slug = models.SlugField(null=True)
    image = models.ImageField(upload_to='uploads', blank=True, null=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.name)
        super(Photo, self).save(force_insert, force_update, using, update_fields)

    class Meta:
        db_tablespace = "pg_default"

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