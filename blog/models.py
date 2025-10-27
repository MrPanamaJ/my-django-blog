from django.db import models
from django.utils import timezone

class Category(models.Model):  # ← СНАЧАЛА определяем Category
    name = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(unique=True, verbose_name='URL')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Post(models.Model):
    #поля модели
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержание')
    create_date = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    published_date = models.DateTimeField(blank=True, null=True, verbose_name='Дата публикации')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='posts', verbose_name='Категория', null=True, blank=True)
    
    # Новые поля для медиа
    image = models.ImageField(upload_to='posts/images/', blank=True, null=True, verbose_name='Главное изображение')
    video = models.FileField(upload_to='posts/videos/', blank=True, null=True, verbose_name='Видео')
    video_poster = models.ImageField(upload_to='posts/video_posters/', blank=True, null=True, verbose_name='Превью видео')
    #методы модели
    def publish(self):
        self.published_date = timezone.now()
        self.is_published = True
        self.save()
        
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

# Create your models here.
