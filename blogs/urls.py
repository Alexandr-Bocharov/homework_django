from django.urls import path

from blogs.apps import BlogsConfig

from blogs.views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView
from django.views.decorators.cache import never_cache

app_name = BlogsConfig.name


urlpatterns = (
    path('', BlogListView.as_view(), name='blog_list'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('create/', never_cache(BlogCreateView.as_view()), name='blog_create'),
    path('edit/<int:pk>/', never_cache(BlogUpdateView.as_view()), name='blog_update'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='blog_delete'),
)