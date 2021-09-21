from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Items(models.Model):
    Item_Name = models.CharField(unique = True,max_length = 101)
    Description = models.TextField(blank = True)
    WholeSale_Price = models.IntegerField()
    Retail_Price = models.IntegerField()
    Picture = models.ImageField(upload_to = 'Pictures')
    all_items = [
        ['Shirts','Shirts'],
        ['Pants','Pants'],
        ['Towels','Towels'],
        ['Pillow_Covers','Pillow_Covers'],
        ['Bed_Sheets','Bed_Sheets'],
        ['Cotton_Sarees','Cotton_Sarees'],
        ['Cotton_Dress','Cotton_Dress'],
        ['Door_Curtains','Door_Curtains']]
    Item_type = models.CharField(max_length = 28,choices = all_items)
    Is_New_Arrival = models.BooleanField(default = True)
    Upload_date = models.DateTimeField(default = timezone.now)
    def __str__(self):
        return self.Item_Name
    class Meta:
        verbose_name = 'Item'

class Cart(models.Model):
    Customer=models.ForeignKey(User,on_delete=models.CASCADE)
    Item_Id=models.ForeignKey(Items,on_delete=models.CASCADE)
    Cart_Item_no = models.AutoField(primary_key=True)
    def __str__(self):
        return str(self.Item_Id)
    class Meta:
        unique_together=('Customer','Item_Id')


class wholesaleuser(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    is_wholesalecustomer = models.BooleanField(default=False)