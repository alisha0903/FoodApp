from django.db import models

# Create your models here.

class Meta:
    app_label  = 'food'
    
class Item(models.Model):
    item_name=models.CharField(max_length=200)
    item_desc=models.CharField(max_length=200)
    item_prce=models.IntegerField(max_length=200)