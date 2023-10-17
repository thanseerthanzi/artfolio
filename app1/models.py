from django.db import models

# Create your models here.
class accounts(models.Model):
    userid = models.CharField(max_length=200)
    status=models.CharField(max_length=200)
    class Meta:
        db_table = 'accounts' 
    
class artist_tbl(models.Model):
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    dob = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    photo=models.CharField(max_length=400)
    state = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    email = models.EmailField()
    pasword = models.CharField(max_length=100)
    class Meta:
        db_table = 'artist_tbl'
    
