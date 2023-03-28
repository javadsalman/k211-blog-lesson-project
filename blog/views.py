from django.shortcuts import render
from .models import Article

# Create your views here.

def blog(request):
    articles = Article.objects.all() # SELECT * FROM blog_article;
    return render(request,'blog.html', context={'articles': articles})

def blog_detail(request, pk):
    article = Article.objects.get(pk=pk)
    return render(request,'blog-detail.html', context={'article': article})

