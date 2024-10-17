from pyexpat.errors import messages

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from pytils.translit import slugify
from django.core.mail import send_mail

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blogs.models import Blog
from django.conf import settings


class BlogListView(ListView):
    model = Blog

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(public_sign=True)

        return queryset



class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()

        return self.object





class BlogCreateView(PermissionRequiredMixin, CreateView):
    model = Blog
    fields = ('title', 'body', 'photo')
    success_url = reverse_lazy('blogs:blog_list')
    permission_required = 'blogs.add_blog'

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()
        return super().form_valid(form)


class BlogUpdateView(PermissionRequiredMixin, UpdateView):
    model = Blog
    fields = ('title', 'body', 'photo')
    success_url = reverse_lazy('blogs:blog_list')
    permission_required = 'blogs.change_blog'

    def get_success_url(self):
        return reverse('blogs:blog_detail', args=[self.kwargs.get('pk')])


class BlogDeleteView(PermissionRequiredMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy('blogs:blog_list')
    permission_required = 'blogs.delete_blog'