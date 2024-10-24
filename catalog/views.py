# from lib2to3.fixes.fix_input import context

from catalog.services import get_cached_categories, get_cached_products
from catalog.models import Category
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.utils.translation.trans_real import catalog
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView

from utils import write_data
from .forms import ProductForm, VersionForm, ProductModeratorForm
from .models import Product, Contacts, Version


class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        return get_cached_products()


    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        for product in context_data['object_list']:
            product.versions = Version.objects.filter(product=product)
            for version in product.versions:
                if version.current_version_flag:
                    product.current_version = version

        return context_data

    def get_queryset(self):
        # для вывода только опубликованных продуктов для обычных пользователей
        if self.request.user.is_staff:
            return Product.objects.all()
        else:
            return Product.objects.filter(is_published=True)


class CategoryListView(ListView):
    model = Category

    def get_queryset(self):
        return get_cached_categories()



class MyProductListView(LoginRequiredMixin, ListView):
    model = Product

    def get_queryset(self):
        return Product.objects.filter(salesman=self.request.user)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    def get_success_url(self):
        return reverse('catalog:product_detail', args=[self.kwargs.get('pk')])

    def get_form_class(self):
        user = self.request.user
        if user == self.object.salesman:
            return ProductForm
        if user.has_perms(['catalog.can_edit_description', 'catalog.can_edit_category', 'catalog.can_cancel_publication']):
            return ProductModeratorForm
        raise PermissionDenied


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'
    model = Contacts
    extra_context = {'object_list': Contacts.objects.all()}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

    success_url = reverse_lazy('catalog:contacts')


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        form.instance.salesman = self.request.user

        return super().form_valid(form)


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')


class VersionCreateView(LoginRequiredMixin, CreateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy('catalog:product_list')


class VersionUpdateView(LoginRequiredMixin, UpdateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy('catalog:product_list')

