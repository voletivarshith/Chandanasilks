from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Items,Cart,wholesaleuser


admin.site.unregister(Group)
admin.site.site_title = 'Chandana Silks'
admin.site.index_title = ''
admin.site.site_header = 'Chandana Silks AdminPage'
admin.site.site_url = '/home/'
#admin.site.register(Cart)
class Customization(admin.ModelAdmin):
    list_filter = ['Item_type','Is_New_Arrival',]
    list_display = ['Item_Name','WholeSale_Price','Retail_Price']
    fieldsets = (
        ('Item Details',{'fields':['Item_Name','WholeSale_Price','Retail_Price','Item_type']}),
        ('Description',{'fields':['Description']}),
        ('Appearance',{'fields':['Picture']}),
        ('New_Arrival',{'fields':['Is_New_Arrival']}),
        ('Date',{'fields':['Upload_date']})

    )


admin.site.register(Items,Customization)

admin.site.register(wholesaleuser)