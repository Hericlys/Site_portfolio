from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.posts_views, name="posts"),
    path('post/<slug:slug>/', views.post_views, name="post")
]
