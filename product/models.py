from django.db import models
from django.utils.translation import gettext_lazy  as _
from django.utils.text import slugify
from django.urls import reverse
# from django.core.urlesolvers import reverse
# Create your models here.

class Product(models.Model):
    PRDName=models.CharField(max_length=100,verbose_name=_("product name:"))
    PRDDesc=models.TextField(max_length=100,verbose_name=_("product decription:"))
    PRDPrice=models.DecimalField(max_digits=5,decimal_places=2,verbose_name=_("product price:"))
    PRDDiscountPrice=models.DecimalField(max_digits=5,decimal_places=2,verbose_name=_("product discountprice:"),blank=True,null=True)
    PRDImage=models.ImageField(upload_to='product/', verbose_name=_("image"),blank=True,null=True)
    PRDCost=models.DecimalField(max_digits=5,decimal_places=2,verbose_name=_("product cost:"))
    PRDCreated=models.DateTimeField(verbose_name=_("product created at:"))
    PRDCategory=models.ForeignKey('Category', verbose_name=_("product category :"), on_delete=models.CASCADE,blank=True,null=True)
    PRDBrand=models.ForeignKey('settings.Brand', verbose_name=_("product brand :"), on_delete=models.CASCADE,blank=True,null=True)
    PRDVarient=models.ForeignKey('settings.Varient', verbose_name=_("product varient :"), on_delete=models.CASCADE,blank=True,null=True)
    PRDSlug=models.SlugField(verbose_name=_("product slug:"), blank=True,null=True)
    PRDNew=models.BooleanField(default=True , blank=True,null=True)
    PRDBestseller=models.BooleanField(default=False , blank=True,null=True)

    # PRDCategory=models.ForeignKey(category,on_delete=models.CASCADE,related_name='product')
    def save(self,*args, **kwargs):
        if not self.PRDSlug:
            self.PRDSlug=slugify(self.PRDName)
        return super(Product,self).save(*args, **kwargs)
    

    class Meta:
        verbose_name = ("product")
        verbose_name_plural = ("products")

    def __str__(self):
        return str(self.PRDName)


    def get_absolute_url(self):
        return reverse("product:product_detail", kwargs={"slug": self.PRDSlug})



# class category , images , alternatives , accessories
class productImage(models.Model):
    PRDIProduct=models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name=_("product"))
    PRDIImage=models.ImageField(upload_to='product/', verbose_name=_("image"))



    class Meta:
        verbose_name = _("productImage")
        verbose_name_plural = _("productImages")

    def __str__(self):
        return str(self.PRDIProduct)

    # def get_absolute_url(self):
    #     return reverse("productImage_detail", kwargs={"pk": self.pk})
class Category(models.Model):
    CATName=models.CharField(max_length=100,verbose_name=_("category name:"))
    CATParent=models.ForeignKey('self',on_delete=models.CASCADE,verbose_name=_("category perant :"),blank=True,null=True,limit_choices_to={'CATParent__isnull':True})
    # limit_choices_to={'CATParent__isnull':True} عشان ميظهرليش في الادمن وانا بختار من الكاتيجوري الساب كاتسجوري 
    CATImg=models.ImageField(upload_to='category/', verbose_name=_("category img"))
    CATDesc=models.TextField(max_length=100,verbose_name=_("category description:"))

    

    class Meta:
        verbose_name = _("category")
        verbose_name_plural = _("categoryies")

    def __str__(self):
        return str(self.CATName)

    # def get_absolute_url(self):
    #     return reverse("category_detail", kwargs={"pk": self.pk})

class Product_ALternative(models.Model):
    PALTProduct=models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name=_("alternative product"),related_name='product_alternative')
    PALTAlternative=models.ManyToManyField(Product,verbose_name=_("alternative"),related_name='alternative')



    class Meta:
        verbose_name = _("Product_ALternative")
        verbose_name_plural = _("Product_ALternatives")

    def __str__(self):
        return str(self.PALTProduct)

    # def get_absolute_url(self):
    #     return reverse("Product_ALternative_detail", kwargs={"pk": self.pk})

class Product_Accessories(models.Model):
    PACCProduct=models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name=_("accessories product"),related_name='product_accessories')
    PACCAccessories=models.ManyToManyField(Product,verbose_name=_("accessories"),related_name='accessories')
    

    class Meta:
        verbose_name = _("Product_accssesories")
        verbose_name_plural = _("Product_accssesories")

    def __str__(self):
        return str(self.PACCProduct)

    # def get_absolute_url(self):
    #     return reverse("Product_accssesories_detail", kwargs={"pk": self.pk})
