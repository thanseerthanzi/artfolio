from django.db import models

# Create your models here.
class guest_tbl(models.Model):
    userid = models.CharField(max_length=200)
    class Meta:
        db_table = 'guest_tbl' 
    
class artist_tbl(models.Model):
    uname = models.CharField(max_length=200)
    pasword = models.CharField(max_length=100)
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    gender = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.BigIntegerField()
    ads = models.CharField(max_length=400)
    district = models.CharField(max_length=100)
    class Meta:
        db_table = 'artist_tbl'
    
