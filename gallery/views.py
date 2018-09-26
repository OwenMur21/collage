from django.http  import HttpResponse
from django.shortcuts import render

def home(request):
    """
    Function that renders the landing page
    """
    return render(request, 'home.html')


