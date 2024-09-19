from lib2to3.fixes.fix_input import context

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils.translation.trans_real import catalog
from django.views.generic import ListView, DetailView, CreateView, TemplateView

from utils import write_data
from .models import Product, Contacts
from .forms import ProductForm



class ProductListView(ListView):
    model = Product


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


class ProductCreateView(CreateView):
    model = Product
    fields = ('name', 'description', 'price', 'category', 'photo')
    success_url = reverse_lazy('catalog:product_list')







