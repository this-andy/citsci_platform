from django.shortcuts import render
from .models import Photo
from .forms import PhotoForm

# from photos.photo_form import PhotoForm
from django.views import generic

# Create your views here.


def photo_list(request):

    photo_list = Photo.objects.all()

    # todo - move this code - it doesn't belong here
    for photo in photo_list:
        photo.extract_image_info()

    context = {'photos': photo_list}

    return render(request, 'photos/photolist.html', context)


class IndexView(generic.ListView):
    template_name = 'photos/photolist.html'
    context_object_name = 'photos'

    def get_queryset(self):
        return Photo.objects.all()


def photo_edit(request):
    form = PhotoForm()
    print('photo_edit')

    if request.method == 'POST':
        form = PhotoForm(data=request.POST)

        if form.is_valid():
            photo = form.save(commit=False)
            if 'image' in request.FILES:
                print('image detected')
                photo.image = request.FILES['image']
            photo.save()
            print('form saved')
            return photo_list(request)
        else:
            print(form.errors)

    return render(request, 'photos/photo_edit.html', {'form': form})


def photo_details(request, photo_slug):
    context = {}

    try:
        photo = Photo.objects.get(slug=photo_slug)
        context['photo'] = photo
    except Photo.DoesNotExist:
        context['photo'] = None

    return render(request, 'photos/photo_detail.html', context)


def photo_zoom(request):
    return render(request, 'photos/photo_zoom.html')
