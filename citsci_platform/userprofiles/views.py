from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import UserProfile


# Create your views here.
def userprofile_list(request):

    up =  UserProfile.objects.first()

    context = {'mobile': up.mobile_phone}

    return render(request, 'userprofiles/userprofilelist.html', context)


def user_profile_details(request):
    up = UserProfile.objects.first()

    context = {}
    return render(request, '', context)


class UserProfileCreateView(LoginRequiredMixin, CreateView):
    model = UserProfile
    fields = ['user', 'mobile_phone', 'nhs_staff']


class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    fields = ['user', 'mobile_phone', 'nhs_staff']


class UserProfileDetailView(LoginRequiredMixin, DetailView):
    model = UserProfile
