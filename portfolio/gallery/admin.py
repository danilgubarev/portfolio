from django.contrib import admin
from django.contrib.admin import ModelAdmin
# from unfold.admin import ModelAdmin  


from .models import Category, Album, Info, Experience, AlbumPhoto, AboutMe

admin.site.register([Info, Experience, AboutMe], ModelAdmin)


class AlbumPhotoInline(admin.TabularInline):
    model = AlbumPhoto
    extra = 0

@admin.register(Album)
class AlbumAdmin(ModelAdmin): 
    inlines = [AlbumPhotoInline]
    exclude = ["slug"]

@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    exclude = ["slug"]
