from django.contrib import admin
from .models import Post, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'create_date', 'is_published', 'has_image', 'has_video')
    list_filter = ('is_published', 'create_date', 'category')
    search_fields = ('title', 'content')
    date_hierarchy = 'create_date'

# Дополнительные методы для отображения в админке
    def has_image(self, obj):
        return bool(obj.image)
    has_image.boolean = True
    has_image.short_description = 'Есть фото'
    
    def has_video(self, obj):
        return bool(obj.video)
    has_video.boolean = True
    has_video.short_description = 'Есть видео'
