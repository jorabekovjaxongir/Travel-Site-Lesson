from django.shortcuts import render


def blogView(request):
    return render(request, 'blog.html')
# Create your views here.
