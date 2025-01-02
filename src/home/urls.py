from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('trained-ia/', views.trained_ia_models, name='trained-ia-models')
]