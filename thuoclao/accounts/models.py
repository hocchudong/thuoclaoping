from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=1024, blank=True)
    city = models.CharField(max_length=100, blank=True)
    website = models.URLField(blank=True)
    phone = models.IntegerField(default=0)
    image = models.ImageField(upload_to='profile_image', blank=True, default='profile_image/user.png')

    def __str__(self):
        return self.user.username


# UserProfile model will be automatically created/updated when we create/update User instances.
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
