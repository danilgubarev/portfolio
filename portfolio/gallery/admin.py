from django.contrib import admin

from .models import Category, Album, Info, Experience, AlbumPhoto, AboutMe
# Register your models here.
admin.site.register([Info, Experience, AboutMe])



class AlbumPhotoInline(admin.TabularInline):
    model = AlbumPhoto
    extra = 0

class AlbumAdmin(admin.ModelAdmin):
    inlines = [AlbumPhotoInline]
    exclude = ["slug"]
@admin.register(Album)

class CategoryAdmin(admin.ModelAdmin):
    exclude = ["slug"]
admin.site.register(Category, CategoryAdmin)

