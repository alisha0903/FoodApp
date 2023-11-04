from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class Meta:
#     app_label  = 'food'

class Item(models.Model):
    user_name=models.Foreignkey(User,on_delete=models.CASCADE,default=1)
    item_name=models.CharField(max_length=200)
    item_desc=models.CharField(max_length=200)
    item_prce=models.IntegerField(max_length=200) 
    item_image = models.CharField(max_length=256,default="https://w7.pngwing.com/pngs/277/489/png-transparent-fast-food-eating-maps-location-placeholder-pin-icon.png" )

    def __str__(self):
        return self.item_name