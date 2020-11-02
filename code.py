# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 07:46:28 2020

@author: Dell India
"""

"""
Definition of models.
"""

fromdjango.dbimportmodels
fromdjango.db.models.signalsimportpost_save
fromdjango.dispatchimport receiver


# Create your models here.
classload(models.Model):
product_name=models.CharField(max_length=200)
product_price=models.IntegerField()
no_of_units=models.IntegerField()
def _str_(self):
returnself.product_name+"("+str(self.product_price)+")"


classpurchase(models.Model):
customer_name= models.CharField(max_length=200)
customer_phone_number= models.CharField(max_length=50)
customer_address= models.CharField(max_length=200)
product_purchased=models.ForeignKey(load,on_delete=models.CASCADE)
no_of_units_purchased=models.IntegerField()
def _str_(self):
returnself.customer_name



@receiver(post_save, sender=purchase )
defupdate_stock(sender, instance, **kwargs):
instance.product_purchased.no_of_units=instance.product_purchased.no_of_units-instance.no_of_units_purchased
instance.product_purchased.save()

fromdjango.contribimport admin
from .modelsimportload,purchase
import csv
fromdjango.httpimportHttpResponse

defexport_as_csv(self, request, queryset):

meta = self.model._meta
field_names = [field.name for field inmeta.fields]

response = HttpResponse(content_type='text/csv')
response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
writer = csv.writer(response)

writer.writerow(field_names)
forobjinqueryset:
row = writer.writerow([getattr(obj, field) for field infield_names])

return response
classloadadmin(admin.ModelAdmin):
actions=[export_as_csv]
list_display=('product_name','product_price','no_of_units')
search_fields=['product_name','product_price','no_of_units']
list_filter=['product_price','no_of_units']
admin.site.register(load, loadadmin)

classpurchaseadmin(admin.ModelAdmin):
actions=[export_as_csv]
search_fields=['customer_name','customer_phone_number','customer_address']
list_display=['customer_name','customer_phone_number','customer_address','product_purchased1','no_of_units_purchased']
def product_purchased1(self, obj):
returnobj.product_purchased.product_name
admin.site.register(purchase, purchaseadmin)