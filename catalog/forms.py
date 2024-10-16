from .models import Product, Version
from django.forms import ModelForm, forms, BooleanField


# class StyleFormMixin:
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for field_name, field in self.fields.items():
#             if isinstance(field, BooleanField):
#                 field.widget.attrs['class'] = 'form-check-input'
#             else:
#                 field.widget.attrs['class'] = 'form-control'


class ProductForm(ModelForm):
    class Meta:
        model = Product
        exclude = ("created_at", "updated_at", 'salesman')

    def clean_name(self):
        name = self.cleaned_data["name"]
        forbidden_words = [
            "казино",
            "криптовалюта",
            "крипта",
            "биржа",
            "дешево",
            "бесплатно",
            "обман",
            "полиция",
            "радар",
        ]
        name_words = name.split()
        for word in name_words:
            if word.lower() in forbidden_words:
                raise forms.ValidationError(
                    f"В названии продукта имеется запрещенное слово: {word}"
                )
        return name

    def clean_description(self):
        description = self.cleaned_data["description"]
        forbidden_words = [
            "казино",
            "криптовалюта",
            "крипта",
            "биржа",
            "дешево",
            "бесплатно",
            "обман",
            "полиция",
            "радар",
        ]
        description_words = description.split()
        for word in description_words:
            if word.lower() in forbidden_words:
                raise forms.ValidationError(
                    f"В описании продукта имеется запрещенное слово: {word}"
                )
        return description

class ProductModeratorForm(ModelForm):
    class Meta:
        model = Product
        fields = ('is_published', 'category', 'description')


class VersionForm(ModelForm):
    class Meta:
        model = Version
        fields = "__all__"

    # def clean_current_version_flag(self):
    #     current_version_flag = self.cleaned_data.get("current_version_flag")
    #     product = Product.objects.get(pk=self.instance.product.pk)
    #     # product_versions = product.version_set.all()
    #
    #     if current_version_flag:
    #         active_version_exists = (
    #             Version.objects.filter(
    #                 product=product,
    #                 current_version_flag=True
    #             )
    #             .exclude(pk=self.instance.pk)
    #             .exists()
    #         )
    #
    #         if active_version_exists:
    #             raise forms.ValidationError(
    #                 "Может быть только одна активная версия продукта."
    #             )
    #
    #     return current_version_flag
