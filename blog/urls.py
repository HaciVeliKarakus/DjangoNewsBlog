from django.urls import path

from .views import BlogListView, AboutView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('about', AboutView.as_view(), name='about'),
    path('post/<int:pk>', BlogDetailView.as_view(), name='post_detail'),
    path('post/new', BlogCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/edit', BlogUpdateView.as_view(), name='post_edit'),
    path('psot/<int:pk>/delete', BlogDeleteView.as_view(), name="post_delete"),
]
