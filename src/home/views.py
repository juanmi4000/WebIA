from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def trained_ia_models(request):
    return render(request, 'trained_ia_models.html')