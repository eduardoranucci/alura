from django.shortcuts import render
from animais.models import Animal

# Create your views here.

def index(request):

    ctx = {
        'caracteristicas': Animal.objects.all()
    }

    return render(request, 'index.html', ctx)
