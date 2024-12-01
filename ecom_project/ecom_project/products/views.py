# products/views.py
from django.shortcuts import render
from django.http import HttpResponse

def product_list(request):
    return HttpResponse("Hello, this is the product list page!")

