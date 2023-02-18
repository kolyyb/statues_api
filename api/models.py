from django.db import models


class Statues(models.Model):
    name = models.CharField(max_length=250)
    date_construct = models.DateField()
    description = models.TextField()
    size = models.IntegerField()
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    img = models.ImageField(upload_to=None)
    rank = models.IntegerField()
    cost = models.CharField(max_length=100)

    def __str__(self):
        return self.name
