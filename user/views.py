from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import CreateUserForm, ProfileUpdateForm, UserUpdateForm


# Create your views here.
def register(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account has been created for {username}. Continue with login!")
            return redirect('user-login')
    else:
        form = CreateUserForm()

    context = {
        "form": form,
    }

    return render(request, 'user/register.html', context)


@login_required
def profile(request):

    return render(request, 'user/profile.html')


@login_required
def profile_update(request):
    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            username = user_form.cleaned_data.get('username')
            messages.success(request, f"Account update for {username} sucessful!")
            return redirect('user-profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        "profile_form": profile_form,
    }

    return render(request, 'user/profile_update.html', context)
