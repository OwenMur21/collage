from django.http  import HttpResponse
from django.shortcuts import render
from .models import Image

def home(request):
    """
    Function that renders the landing page
    """
    images = Image.get_images()
    return render(request, 'home.html', {"images":images})

