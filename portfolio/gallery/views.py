from django.shortcuts import render
from .models import Album, Category, Info, Experience, AlbumPhoto

# Create your views here.
def index(request):
    context = {
        'category' : Category.objects.all(),
        'albums' : Album.objects.all()[0:6],
        'last_photo': AlbumPhoto.objects.last(),
        'experience' : Experience.objects.first(),
        'info': Info.objects.first()
        
    }
    return render(request, 'gallery/index.html', context)