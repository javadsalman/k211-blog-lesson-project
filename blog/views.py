from django.shortcuts import render
from .models import Article, Author, Tag

# Create your views here.

def blog(request):
    articles = Article.objects.all()
    authors = Author.objects.all()
    tags = Tag.objects.all()
    author_username = request.GET.get('author')
    tag_title = request.GET.get('tag')
    if author_username:
        articles = articles.filter(author__user__username=author_username)
    if tag_title:
        articles = articles.filter(tags__title=tag_title)
    return render(request,'blog.html', context={
        'articles': articles, 
        'authors': authors,
        'tags': tags
    })

def blog_detail(request, pk):
    article = Article.objects.get(pk=pk)
    return render(request,'blog-detail.html', context={'article': article})

