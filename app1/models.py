from django.db import models

# Create your models here.
class accounts(models.Model):
    userid = models.CharField(max_length=200)
    status=models.CharField(max_length=200)
    class Meta:
        db_table = 'accounts' 
    
class artist_tbl(models.Model):
    uname = models.CharField(max_length=200)
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    gender = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.BigIntegerField()
    ads = models.CharField(max_length=400)
    photo=models.CharField(max_length=400)
    district = models.CharField(max_length=100)
    class Meta:
        db_table = 'artist_tbl'
    
