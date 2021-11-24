from django.contrib.auth import (
    get_user_model,
    authenticate,
    login as login_user,
    logout as logout_user
)
from django.shortcuts import render, redirect
from django.urls import reverse

from apps.authentication.forms import RegistrationForm, LoginForm


User = get_user_model()


def registration(request):
    if request.user.is_authenticated:
        return redirect(reverse('catalog:home'))

    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password2'])
            user.save()
            return redirect(reverse('catalog:home'))
    else:
        form = RegistrationForm()
    return render(
        request,
        'authentication/registration.html',
        {'form': form}
    )


def login(request):
    if request.user.is_authenticated:
        return redirect(reverse('catalog:home'))

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user:
                login_user(request, user)
                return redirect(reverse('catalog:home'))
    else:
        form = LoginForm()
    return render(
        request,
        'authentication/login.html',
        {'form': form}
    )


def logout(request):
    logout_user(request)
    return redirect(reverse('catalog:home'))
