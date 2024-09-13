from .models import Product
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, ImageField, ClearableFileInput, NumberInput, DateInput


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'photo', 'price', 'created_at', 'updated_at']

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название продукта'
            }),
            'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание'
            }),
            'price': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цена',
                'min': 0,
                'step': 1
            }),
            'photo': ClearableFileInput(attrs={
                'class': 'form-control-file',
                'placeholder': 'Выбрать фото',
                'accept': 'image/*'
            })


        }