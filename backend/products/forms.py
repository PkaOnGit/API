from django import forms
from .models import Product

class ProductForm(forms.Model.Form):
    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price'
        ]