from django.shortcuts import render
from django.forms.models import model_to_dict
from django.http import JsonResponse
import json
from products.models import Product

# Create your views here.

def api_home(request):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data = model_to_dict(model_data, fields=['title'])
    return JsonResponse(data)
