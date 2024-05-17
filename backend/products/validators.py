from rest_framework import serializers
from .models import Product
from rest_framework.validators import UniqueValidator



# def validated_title(value):
#     qs = Product.objects.filter(title_iexact=value)# using iexact is better than exact for sensitive validation
#     if qs.exists():
#         raise serializers.ValidationError(f"{value} is a product name")
#     return value

def validate_title_no_hello(value):
    if "hello" in value.lower():
        raise serializers.ValidationError(f"{value} No hello")
    return value

unique_product_title = UniqueValidator(queryset=Product.objects.all(), lookup = 'iexact')