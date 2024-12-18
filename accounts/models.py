from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy  as _
from django.utils.text import slugify
from django.contrib.auth.models import User
import datetime
from django.db.models.signals import post_save
from django_countries.fields import CountryField
# Create your models here.

class Profile(models.Model):
    uesr=models.OneToOneField(User, verbose_name=_("user"), on_delete=models.CASCADE)
    slug=models.SlugField(blank=True,null=True)
    country=CountryField()
    join_date=models.DateTimeField( default=datetime.datetime.now)
    address=models.CharField( max_length=50)
    image=models.ImageField( upload_to='user_image/',blank=True,null=True)

    

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")

    def __str__(self):
        return str(self.uesr)
# for moveing
    def get_absolute_url(self):
        return reverse("accounts:Profile_detail", kwargs={"slug": self.slug})
    # for slug
    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.uesr.username)
        return super(Profile,self).save(*args, **kwargs)
    # for signals
    def create_profile(sender, **kwargs):
        if kwargs['created']:
            user_profile=Profile.objects.create(uesr=kwargs['instance'])
    post_save.connect(create_profile,sender=User)        