from django.shortcuts import render, get_object_or_404, redirect
from utils import write_data
from .models import Product, Contacts
from .forms import ProductForm


def home(request):
    products = Product.objects.order_by('-id')[:5]
    for prod in products:
        print(prod)
    return render(request, 'main/home.html', {'products': products})


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        info = {
            "name": name,
            "phone": phone,
            "message": message
        }

        write_data(info)

    contacts = Contacts.objects.all()
    return render(request, 'main/contacts.html', {'contacts': contacts})


def product(request, pk):
    prod = get_object_or_404(Product, pk=pk)
    context = {
        'product': prod
    }
    return render(request, 'main/product.html', context)


def ProductDetailView(UpdateView):
    model = Product
    template_name = 'main/create.html'


def create(request):
    error = ''
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalog:home')
        else:
            error = 'Форма была неверной'


    form = ProductForm()
    context = {'form': form,
               'error': error}

    return render(request, 'main/create.html', context)




