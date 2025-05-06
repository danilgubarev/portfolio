from django.db import models
from multiupload.fields import MultiImageField
from django.core.exceptions import ValidationError
from django.utils.text import slugify

class Category(models.Model):
    TYPE_OF_CONTENT = {
        ('video', 'Відео'),
        ('photo', 'Фото'),
    }
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='category_images/')
    description = models.TextField(null=True, blank=True)
    type_of_content = models.CharField(choices=TYPE_OF_CONTENT, default='photo')
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

class Album(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, models.CASCADE, related_name='categories')
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
class AlbumPhoto(models.Model):
    album = models.ForeignKey(Album, models.CASCADE, related_name='photos')
    images = models.ImageField(upload_to='album/', null=True, blank=True)
    video_url = models.URLField(null=True, blank=True)

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
