from django.shortcuts import render
from django.conf import settings
import json
import os

# Create your views here.
def index(request):
    json_ruta = os.path.join(settings.BASE_DIR, 'home/static/json/habilidades.json')
    with open(json_ruta) as habilidades_json:
        habilidades = json.load(habilidades_json)
    return render(request, 'index.html', {'habilidades': habilidades})

def trained_ia_models(request):
    return render(request, 'trained_ia_models.html')