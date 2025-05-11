from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),
    path('post/add/', views.add_post, name='add-post'),
    path('posts/<post_slug>/', views.post_detail, name='post-detail'),
]
