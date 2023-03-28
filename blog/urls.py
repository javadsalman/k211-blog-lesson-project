from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [ 
    path('', views.blog, name='article-list'),
    path('<int:pk>/',views.blog_detail, name='article-detail'),
]
