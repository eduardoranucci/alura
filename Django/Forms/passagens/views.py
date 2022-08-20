from ast import Pass
from django.shortcuts import render
from passagens.forms import PassagemForm

# Create your views here.

def index(request):

    form = PassagemForm()

    ctx = {
        'form': form
    }
    
    return render(request, 'index.html', ctx)

def revisao(request):

    if request.method == 'POST':

        form = PassagemForm(request.POST)

        ctx = {
            'form' : form
        }

        return render(request, 'revisao.html', ctx)
