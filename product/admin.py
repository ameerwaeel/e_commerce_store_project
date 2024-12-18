from django.contrib import admin

# Register your models here.
from .models import *
  


admin.site.register(Product)  
admin.site.register(productImage) 
admin.site.register(Category)      
admin.site.register(Product_ALternative) 
admin.site.register(Product_Accessories) 


