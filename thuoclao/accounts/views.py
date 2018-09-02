from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.admin.models import LogEntry
from django.contrib.auth import (
    authenticate,
    login,
)

from .forms import UserForm, UserProfileForm, UserRegisterForm


def register(request):
    if request.user.is_authenticated:
        return redirect("/")
    form = UserRegisterForm(request.POST or None)
    print(form.is_valid())
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        authenticate(username=user.username, password=user.password)
        login(request, user)
        return redirect("/")
    return render(request, 'accounts/reg_form.html', {"form": form})


def view_profile(request, pk=None):
    form = UserProfileForm()
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
        log = LogEntry.objects.select_related().all().order_by("id")
    context = {'user': user, 'form': form, 'log': log}
    return render(request, 'accounts/profile.html', context)


def edit_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            if request.FILES:
                handle_uploaded_file(request.FILES['image'])
            user_form.save()
            profile_form.save()
    return HttpResponseRedirect(reverse('view_profile'))


def handle_uploaded_file(f):
    """
    Write file uploaded
    """
    path = "thuoclao/media/profile_image/" + f.name
    file = open(path, 'wb+')
    for chunk in f.chunks():
        file.write(chunk)
    file.close()
