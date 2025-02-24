from django.shortcuts import render
from .models import About, Categories, Guide

def aboutView(request):
    return render(request, 'about.html',context={
        'abouts' : About.objects.first(),
        'categories' : Categories.objects.all(),
        'guides' : Guide.objects.all(),
    })

# Create your views here.
