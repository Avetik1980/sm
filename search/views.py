from django.shortcuts import render
from .forms import UserSearchForm
from users.models import UserProfile

def search(request):
    if request.method == 'POST':
        form = UserSearchForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            social_network = form.cleaned_data['social_network']
            # Adjust the query based on the selected social network
            if social_network == 'all':
                results = UserProfile.objects.filter(user__username__icontains=username)
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
    else:
        form = UserSearchForm()
        results = None
    return render(request, 'search/search.html', {'form': form, 'results': results})
