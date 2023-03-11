from rest_framework import serializers
from products.models import *


class ProductsSerializer(serializers.ModelSerializer):
    offer_price = serializers.SerializerMethodField()
    product_image = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'description',
            'price',
            'offer',
            'offer_price',
            'product_image',
        )
    def get_offer_price(self,instance):
        price = instance.price
        offer = instance.offer
        discount = (price * offer)/100
        offer_price = price - discount
        return offer_price
    
    def get_product_image(self,instance):
        request = self.context['request']
        if ProductImages.objects.filter(product = instance).exists():
            instances = ProductImages.objects.filter(product = instance)
            product_image = ProductImageSerializer(
                instances,
                context = {
                "request":request
                },
                many = True
            ).data
        else:
            product_image = None
        return product_image


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImages
        fields = (
            'image',
            'is_cover',
        )