from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, SearchForm
from django.contrib.auth.decorators import login_required
from notifications.models import DetailRequest


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    accepted_requests = request.user.received_requests.filter(accepted=True)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'accepted_requests': accepted_requests
    }

    return render(request, 'users/profile.html', context)


@login_required
def recipient_list(request):
    sent_requests = request.user.sent_requests.filter(accepted=True)
    return render(request, 'users/recipients.html', {'requests': sent_requests})


@login_required
def donator_list(request):
    received_requests = request.user.received_requests.filter(accepted=True)
    return render(request, 'users/donators.html', {'requests': received_requests})


def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            social_network = form.cleaned_data['social_network']
            return render(request, 'users/search_results.html',
                          {'username': username, 'social_network': social_network})
    else:
        form = SearchForm()
    return render(request, 'users/search.html', {'form': form})
