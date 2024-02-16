from django.contrib.auth.models import User
from django.db import models
import uuid
import hashlib
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import RegexValidator


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics', blank=True)
    wallet_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    hashed_user_id = models.CharField(max_length=255, unique=True, editable=False)

    twitter_id = models.CharField(max_length=255, blank=True, null=True)
    twitter_verified = models.BooleanField(default=False)

    facebook_id = models.CharField(max_length=255, blank=True, null=True)
    facebook_verified = models.BooleanField(default=False)

    reddit_id = models.CharField(max_length=255, blank=True, null=True)
    reddit_verified = models.BooleanField(default=False)

    instagram_id = models.CharField(max_length=255, blank=True, null=True)
    instagram_verified = models.BooleanField(default=False)

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True,
                                    null=True)  # Validators is a list

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        if not self.hashed_user_id:
            self.hashed_user_id = hashlib.sha256(str(uuid.uuid4()).encode()).hexdigest()
        super(UserProfile, self).save(*args, **kwargs)

    def has_social_media_linked(self):
        return any([self.twitter_id, self.facebook_id, self.reddit_id, self.instagram_id])

    def has_verified_social_media(self):
        return any([self.twitter_verified, self.facebook_verified, self.reddit_verified, self.instagram_verified])


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    UserProfile.objects.get_or_create(user=instance)
