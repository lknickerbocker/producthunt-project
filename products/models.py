from django.db import models
import datetime
from django.contrib.auth.models import User

class Product(models.Model):
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=500)
    pub_date = models.DateTimeField()
    votes_total = models.IntegerField(default =1)
    image = models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='image/')
    body = models.CharField(max_length=1000)
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self): ###object title in database
        return self.title

    def summary(self): ####createsanewbodylimited to 100
        return self.body[:100]

    def pub_date_pretty(self): #customizes our date/time
        return self.pub_date.strftime('%b %e %Y')
