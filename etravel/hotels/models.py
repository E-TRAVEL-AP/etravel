from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.forms import ModelForm
#from star_ratings.models import Rating

#######################################################################################################################################

class Hotel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=True)
    median_price = models.FloatField()
    description = models.CharField(max_length=5000, null=True)
    image = models.ImageField(null=True, blank=True)
    location = models.CharField(max_length=200, null=True)
    covid_friendly = models.BooleanField(default=False, null=True, blank=False)
    #category
    #star_rating = models.OneToOneField(Rating, on_delete=models.CASCADE, related_query_name = 'hotel')

    def __str__(self):
        return self.name

    @property

    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

#Hotel.objects.filter(ratings__isnull=False).order_by('ratings__average')

#######################################################################################################################################

class Room(models.Model):
    room_number = models.IntegerField(null=False, blank=False, default=0)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    median_price = models.FloatField()
    description = models.CharField(max_length=5000, null=True)
    image = models.ImageField(null=True, blank=True)
    #room_type
    #air_conditioned = models.BooleanField(default=False, null=True, blank=False)

    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    def __str__(self):
        return (f'{self.hotel}-{self.room_number}')

 #######################################################################################################################################

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    comment = models.CharField(max_length=5000, null=True)
    #rating = 

#######################################################################################################################################

class Reservation(models.Model):
    reservation_id = models.IntegerField(null=False, blank=False, default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    checkin_date = models.DateField()
    checkout_date = models.DateField()
    booked_on = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return (f'{self.room}-{self.reservation_id}')
