from django.db import models

# Create your models here.

# every model is a Python class
# a model for each table

class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)
    
    def __str__(self):
        return f"{self.city} ({self.code})"
    
class Flights(models.Model):
    #origin = models.CharField(max_length=64)
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    #destination = models.CharField(max_length=64)
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()
    
    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"

class Passenger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    flights = models.ManyToManyField(Flights, blank=True, related_name="passenger")
    
    def __str__(self):
        return f"{self.first} {self.last}"