from django.urls import path
from . import views

urlpatterns = [
    path('', views.single_page, name='home'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
]
