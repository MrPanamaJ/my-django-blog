from django.shortcuts import render, get_object_or_404
from .models import Post, Category  # ← Добавить Category в импорт

def home(request):
    posts = Post.objects.filter(is_published=True).order_by('-create_date')
    categories = Category.objects.all()
    return render(request, 'blog/home.html', {
        'posts': posts,
        'categories': categories
    })

def about(request):
    categories = Category.objects.all()  # ← Добавить категории для меню
    return render(request, 'blog/about.html', {'categories': categories})

def post_detail(request, pk):  # ← Изменить post_id на pk
    post = get_object_or_404(Post, id=pk, is_published=True)  # ← id=pk вместо id=post_id
    categories = Category.objects.all()  # ← Добавить для меню
    return render(request, 'blog/post_detail.html', {
        'post': post,
        'categories': categories
    })

def category_posts(request, slug):
    category = Category.objects.get(slug=slug)
    posts = Post.objects.filter(category=category, is_published=True).order_by('-create_date')
    categories = Category.objects.all()
    return render(request, 'blog/category_posts.html', {
        'category': category,
        'posts': posts,
        'categories': categories
    })