from lib2to3.fixes.fix_input import context

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.utils.translation.trans_real import catalog
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView

from utils import write_data
from .forms import ProductForm, VersionForm
from .models import Product, Contacts, Version


class ProductListView(ListView):
    model = Product

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        for product in context_data['object_list']:
            product.versions = Version.objects.filter(product=product)
            for version in product.versions:
                if version.current_version_flag:
                    product.current_version = version




        return context_data

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    login_url = "/users/login/"
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    def get_success_url(self):
        return reverse('catalog:product_detail', args=[self.kwargs.get('pk')])


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'
    model = Contacts
    extra_context = {'object_list': Contacts.objects.all()}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

    success_url = reverse_lazy('catalog:contacts')





# def contacts(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         phone = request.POST.get('phone')
#         message = request.POST.get('message')
#
#         info = {
#             "name": name,
#             "phone": phone,
#             "message": message
#         }
#
#         write_data(info)

    # contacts = Contacts.objects.all()
    # return render(request, 'catalog/contacts.html', {'contacts': contacts})


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    login_url = "/users/login/"
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        form.instance.salesman = self.request.user

        return super().form_valid(form)

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    login_url = "/users/login/"
    model = Product
    success_url = reverse_lazy('catalog:product_list')


class VersionCreateView(LoginRequiredMixin, CreateView):
    login_url = "/users/login/"
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy('catalog:product_list')


class VersionUpdateView(UpdateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy('catalog:product_list')










