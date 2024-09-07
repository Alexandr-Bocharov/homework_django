from django.shortcuts import render
from utils import write_data
from .models import Product, Contacts


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



