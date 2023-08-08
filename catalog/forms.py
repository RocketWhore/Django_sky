from django import forms
from catalog.models import Product, Version


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        # field = ('title', 'price')
        exclude = ()

    def clean_title(self):
        cleaned_data = self.cleaned_data['title']

        for title in cleaned_data.strip().split():
            if title.lower() in ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                                 'радар']:
                raise forms.ValidationError('Вы пытаетесь создать запрещенный продукт')

        return cleaned_data


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        exclude = ()