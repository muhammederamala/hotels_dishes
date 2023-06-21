from django.db import models

class Hotel_model(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    items = models.TextField()
    lat_long = models.CharField(max_length=255)
    full_details = models.TextField()

    def __str__(self):
        return self.name
