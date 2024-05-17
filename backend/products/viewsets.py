from rest_framework import viewsets, mixins
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk' #defualt

class ProductGenericViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk' #defualt

# product_list_view = ProductGenericViewSet.as_view({'get':'retrieve'})
# product_list = ProductGenericViewSet.as_view({'get':'list'})
