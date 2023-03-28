from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    
    def __str__(self):
        return self.user.username

class Tag(models.Model):
    title = models.CharField(max_length=10)
    
    def __str__(self):
        return self.title

class Article(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)
    content = models.TextField()
    show = models.BooleanField(default=True)
    tags = models.ManyToManyField(Tag)
    view_count = models.IntegerField()
    main_image = models.ImageField(null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    