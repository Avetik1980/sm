from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)  # Add an email field to the form

    class Meta:
        model = User  # Specify which model will be used to create the user
        fields = ['username', 'email', 'password1', 'password2']  # Include these fields in the form

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_picture', 'twitter_id', 'facebook_id', 'instagram_id', 'reddit_id', 'phone_number']

class SearchForm(forms.Form):
    SOCIAL_CHOICES = (
        ('all', 'All'),
        ('fb', 'Facebook'),
        ('ig', 'Instagram'),
        ('tw', 'Twitter'),
        ('rd', 'Reddit'),
    )

    username = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    social_network = forms.ChoiceField(choices=SOCIAL_CHOICES, required=False)
