from django.shortcuts import render
from utils import write_data


def home(request):
    return render(request, 'main/home.html')


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

    return render(request, 'main/contacts.html')



