from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView, DeleteView

from .models import Post


class BlogListView(ListView):
    model = Post
    template_name = "post/home.html"
    context_object_name = "all_post_list"


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post/post_detail.html'


class BlogCreateView(CreateView):
    model = Post
    template_name = 'post/post_create.html'
    fields = '__all__'


class BlogUpdateView(UpdateView):
    model = Post
    template_name = "post/post_edit.html"
    fields = ["title", "body"]


class BlogDeleteView(DeleteView):
    model = Post
    template_name = "post/post_delete.html"
    success_url = reverse_lazy("home")


class AboutView(TemplateView):
    template_name = "about.html"
