from django.db import models
from django.urls import reverse 
from django.contrib.auth.models import User 

# Create your models here.
class Room(models.Model): 
    name        = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    description2 = models.TextField(blank=True, null=True)
    price       = models.DecimalField(decimal_places=2, max_digits=10000)
    person      = models.CharField(max_length=120)
    size        = models.IntegerField()
    bed         = models.IntegerField()
    image       = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self): 
        return reverse("room-detail", kwargs={"id": self.id}) #f"/products/{self.id}/"booking
 
    
class Convenience(models.Model): 
    name       = models.CharField(max_length=120)
    UrlConvPic  = models.CharField(max_length=1000)
    rooms       = models.ManyToManyField(Room , through='RoomConv' , through_fields=('convenience','room'),  )
    def __str__(self):
        return self.name

class Photo(models.Model): 
    
    UrlPic      = models.CharField(max_length=1000)
    idRoom      = models.ForeignKey(Room , on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.name
    
class RoomConv (models.Model): 
    convenience = models.ForeignKey(Convenience ,on_delete=models.CASCADE )    
    room = models.ForeignKey(Room ,on_delete=models.CASCADE )
    relation = models.ForeignKey(
        Room,
        on_delete=models.CASCADE,
        related_name="RoomConv",
    )
class Booking (models.Model): 
    date_in  = models.DateField()
    date_out = models.DateField()
    client   = models.ForeignKey(User , null=True ,default=None,on_delete=models.CASCADE)
    person   = models.IntegerField()
    room     = models.ForeignKey(Room , null=True , on_delete=models.CASCADE )  

    