from storeapi_app.models import Product
from storeapi_app.api.serializers import ProductSerializer
from rest_framework import generics, filters



class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['=featured', '=company', '$name']
    
    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Product.objects.all()
        featured = self.request.query_params.get('featured')
        if featured is not None:
            queryset = queryset.filter(featured=featured)
        return queryset
