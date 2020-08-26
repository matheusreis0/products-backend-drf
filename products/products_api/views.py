from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer

# Create your views here.
class ProductApi(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('created_at')
    serializer_class = ProductSerializer
