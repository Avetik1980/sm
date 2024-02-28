from django import forms

SOCIAL_NETWORK_CHOICES = [
    ('all', 'All'),
    ('fb', 'Facebook'),
    ('ig', 'Instagram'),
    ('tw', 'Twitter'),
    ('rd', 'Reddit'),
]

class UserSearchForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    social_network = forms.ChoiceField(choices=SOCIAL_NETWORK_CHOICES)
