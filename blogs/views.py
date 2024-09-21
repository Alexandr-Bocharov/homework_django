from pyexpat.errors import messages

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

        # if self.object.views_count == 100:
        #     self.send_congratulations_email()

        return self.object

    # def send_congratulations_email(self):
    #     subject = f'Статья {self.object.title} достигла 100 просмотров!'
    #     message = f'Поздравляем! Ваша статья {self.object.title} набрала 100 просмотров!'
    #     from_email = settings.DEFAULT_FROM_EMAIL
    #     recipient_list = ['counter2306@yandex.ru']
    #
    #     send_mail(subject, message, from_email, recipient_list)




class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'body', 'photo')
    success_url = reverse_lazy('blogs:blog_list')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()
        return super().form_valid(form)


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'body', 'photo')
    success_url = reverse_lazy('blogs:blog_list')

    def get_success_url(self):
        return reverse('blogs:blog_detail', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blogs:blog_list')