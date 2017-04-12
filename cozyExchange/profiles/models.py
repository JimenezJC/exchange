from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from allauth.account.signals import user_logged_in, user_signed_up

import stripe
stripe.api_key = settings.STRIPE_SECERT_KEY

class profile(models.Model):
    name = models.CharField(max_length = 20)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, null = True, blank = True)
    location = models.CharField(
        max_length = 40,
        default=''
    )
    bio = models.TextField(default='')
    rating = models.FloatField(
        default = 3.0,
        validators=[MaxValueValidator(5.0), MinValueValidator(0.0)]
    )
    verifiedStore = models.BooleanField (default = False)
    if( verifiedStore ):
        storeName = models.CharField(
            max_length = 20,
            default = '',
            blank = True
        )
    #Item/list

    def __str__(self):
        return self.name

class userStripe(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    stripe_id = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        if self.stripe_id:
            return str(self.stripe_id)
        else:
            return self.user.username

def stripeCallback(sender, request, user, **kwargs):
    user_stripe_account, created = userStripe.objects.get_or_create(user=user)
    if created:
        print('created for%s' %(user.username))
    if user_stripe_account.stripe_id is None or user_stripe_account.stripe_id == '':
        new_stripe_id = stripe.Customer.create(email=user.email)
        user_stripe_account.stripe_id = new_stripe_id['id']
        user_stripe_account.save()

def profileCallback(sender, request, user, **kwargs):
    userProfile, is_created = profile.objects.get_or_create(user=user)
    if is_created:
        userProfile.name = user.username
        userProfile.save()

user_logged_in.connect(stripeCallback)
user_signed_up.connect(profileCallback)
user_signed_up.connect(stripeCallback)
