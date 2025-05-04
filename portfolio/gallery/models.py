from django.db import models
from multiupload.fields import MultiImageField
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='category_images/')
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Album(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, models.CASCADE, related_name='categories')

    def __str__(self):
        return self.name
    
class AlbumPhoto(models.Model):
    category = models.ForeignKey(Album, models.CASCADE, related_name='photos')
    images = models.ImageField(upload_to='album/')

class Info(models.Model):
    title = models.CharField(max_length=160)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
    
class AboutMe(models.Model):
    image = models.ImageField(upload_to='aboutme_image/', null=True, blank=True)
    description = models.TextField()

class Experience(models.Model):
    years_exp = models.PositiveIntegerField()
    drone_flights = models.PositiveIntegerField()
    total_shoots = models.PositiveIntegerField()
    
    def __str__(self):
        return f'{self.years_exp}, {self.drone_flights}, {self.total_shoots}'
