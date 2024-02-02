# from django import forms

from .models import Product


# class ProductForm(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = [
#             "title",
#             "content",
#             "price"
#         ]

from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "title",
            "content",
            "price",
            "sale_price",
            "name",
        ]
