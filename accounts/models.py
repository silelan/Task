from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext as _
import uuid 
from django_countries.fields import CountryField

from django.utils.safestring import mark_safe

class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.email

class Address(models.Model):
    street_address = models.CharField('StreetAddress', max_length = 250)
    city = models.CharField('city', max_length = 50)
    state = models.CharField('state', max_length= 50)
    pincode = models.CharField('pincode', max_length=10)
    country = CountryField()
    
    def __str__(self):
        return self.street_address

class Profile(models.Model):

    GENDER_CHOICES = (
        ('M', 'male'),
        ('F', 'female'),
        ('O', 'other')
    )
    user = models.OneToOneField(CustomUser, on_delete = models.CASCADE,related_name='profile')
    phone_number = models.CharField(unique = True, max_length=20,default=uuid.uuid4)
    profile_picture = models.ImageField(upload_to='profile_picture/',blank=True)
    gender = models.CharField(max_length = 2, choices = GENDER_CHOICES)
    date_of_birth = models.DateTimeField(null = True, blank = True)
    friends = models.ManyToManyField("self")
    slug = models.SlugField()
    permanent_address = models.OneToOneField(Address, on_delete = models.CASCADE, related_name = 'permanent_address',null=True)
    company_address = models.OneToOneField(Address, on_delete = models.CASCADE, related_name = 'company_address',null=True)

    USERNAME_FIELD = 'user.email'
    REQUIRED_FIELDS = []

    def __str__(self, name): 
        return self.user.username

    def get_absolute_url(self):
    	return "/users/{}".format(self.slug)

@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
 
@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

post_save.connect(create_user_profile, sender=settings.AUTH_USER_MODEL)


class FriendRequest(models.Model):
	to_user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete = models.CASCADE, related_name='to_user')
	from_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='from_user',on_delete = models.CASCADE)
	timestamp = models.DateTimeField(auto_now_add=True) # set when created 

	def __str__(self):
		return "From {}, to {}".format(self.from_user.username, self.to_user.username)