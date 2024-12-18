from django.db import models
from django.utils.translation import gettext_lazy  as _

# Create your models here.


class Brand(models.Model):
    BRDName=models.CharField( max_length=50,verbose_name='brand name')
    BRDDesk=models.TextField(max_length=200,null=True,blank=True,verbose_name='brand description')

    

    class Meta:
        verbose_name = _("Brand")
        verbose_name_plural = _("Brands")

    def __str__(self):
        return str(self.BRDName)

    # def get_absolute_url(self):
    #     return reverse("Brand_detail", kwargs={"pk": self.pk})
class Varient(models.Model):
    VARName=models.CharField( max_length=50,verbose_name='varient name')
    VARDesk=models.TextField(max_length=200,null=True,blank=True,verbose_name='varient description')

    

    class Meta:
        verbose_name = _("varient")
        verbose_name_plural = _("varients")

    def __str__(self):
        return str(self.VARName)

    # def get_absolute_url(self):
    #     return reverse("Brand_detail", kwargs={"pk": self.pk})
