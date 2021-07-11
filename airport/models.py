from django.db import models


# All the models and it's same as database table
# Surface table
class Surface(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.CharField()
    condition = models.TextField()

    # Return instance surface
    def __str__(self):
        return f'Surface number: {self.id}'


# Runway table
class Runway(models.Model):
    id = models.IntegerField(primary_key=True)
    number = models.IntegerField()
    width = models.IntegerField()
    length = models.IntegerField()
    surface = models.OneToOneField(Surface, on_delete=models.CASCADE)

    # Return instance runway
    def __str__(self):
        return f'Runway id: {self.id}'


# Airport table
class Airport(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField()
    runway = models.ForeignKey(Runway, on_delete=models.CASCADE)

    # Return instance airport
    def __str__(self):
        return f'Airport name: {self.name}'