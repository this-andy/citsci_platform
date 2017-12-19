from django import forms
from citsci_platform.photos.models import Photo


class PhotoForm(forms.ModelForm):

    name = forms.CharField(max_length=100)
    latitude = forms.FloatField(max_value=180, min_value=-180)
    longitude = forms.FloatField(max_value=180, min_value=-180)
    image = forms.ImageField()

    class Meta:
        model = Photo
        fields = ('name', 'image', 'latitude', 'longitude', )
