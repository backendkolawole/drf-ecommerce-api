from rest_framework import serializers
from storeapi_app.models import Product


    
    
class ProductSerializer(serializers.ModelSerializer):
    MY_CHOICES = ['ikea', 'liddy', 'caressa', 'marcos']

    company = serializers.ChoiceField(choices=MY_CHOICES)
    
    class Meta:
        model = Product
        fields = "__all__"
