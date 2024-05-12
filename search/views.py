from django.shortcuts import render
from django.db import models
from users.forms import SearchForm
from users.models import UserProfile

def search(request):
    form = SearchForm()
    results = None
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            social_network = form.cleaned_data['social_network']
            # Adjust the query based on the selected social network
            if social_network == 'all':
                results = UserProfile.objects.filter(
                    models.Q(facebook_id__icontains=username) |
                    models.Q(instagram_id__icontains=username) |
                    models.Q(twitter_id__icontains=username) |
                    models.Q(reddit_id__icontains=username)
                )
            else:
                # Adjust these queries based on your UserProfile model's fields
                field_map = {
                    'fb': 'facebook_id',
                    'ig': 'instagram_id',
                    'tw': 'twitter_id',
                    'rd': 'reddit_id',
                }
                filter_kwargs = {f"{field_map[social_network]}__icontains": username}
                results = UserProfile.objects.filter(**filter_kwargs)
    return render(request, 'search/search.html', {'form': form, 'results': results})
