from django.shortcuts import render
from .models import UserProfile


# Create your views here.
def userprofile_list(request):

    up =  UserProfile.objects.first()

    context = {'mobile': up.mobile_phone}

    return render(request, 'userprofiles/userprofilelist.html', context)
