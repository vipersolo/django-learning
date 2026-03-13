from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Catergory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Actor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="movies")
    title = models.CharField(max_length=200)
    poster = models.ImageField(upload_to="posters/")
    description = models.TextField()
    release_date = models.DateField()
    actors = models.ManyToManyField(Actor,related_name="movies_by_actor")
    rating = models.DecimalField(max_digits=2,decimal_places=1)
    catergory = models.ForeignKey(Catergory,on_delete=models.CASCADE,related_name="movies_cat")
    trailer = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    


