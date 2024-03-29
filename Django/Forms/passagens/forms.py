from datetime import datetime
from django import forms
from tempus_dominus.widgets import DatePicker
from passagens.classe_viagem import tipos_de_classe
from passagens.validation import *

# Utilizado models

from passagens.models import Passagem, ClasseViagem, Pessoa

class PassagemForm(forms.ModelForm):

    data_pesquisa = forms.DateField(label='Data da pesquisa', disabled=True, initial=datetime.today)

    class Meta:

        model = Passagem
        fields = '__all__'
        labels = {
            'data_ida': 'Data de ida',
            'data_volta': 'Data de volta',
            'data_pesquisa': 'Data da pesquisa',
            'classe_viagem': 'Classe do vôo',
            'informacoes': 'Informações'
        }
        widgets = {
            'data_ida': DatePicker(),
            'data_volta': DatePicker()
        }


    def clean(self):

        origem = self.cleaned_data.get('origem')
        destino = self.cleaned_data.get('destino')
        data_ida = self.cleaned_data.get('data_ida')
        data_volta = self.cleaned_data.get('data_volta')
        data_pesquisa = self.cleaned_data.get('data_pesquisa')

        lista_erros = {}

        campo_tem_numero(origem, 'origem', lista_erros)
        campo_tem_numero(destino, 'destino', lista_erros)
        origem_destino_iguais(origem, destino, lista_erros)
        volta_menor_que_ida(data_ida, data_volta, lista_erros)
        ida_menor_que_hoje(data_ida, data_pesquisa, lista_erros)

        if lista_erros is not None:

            for erro in lista_erros:

                msg = lista_erros[erro]
                self.add_error(erro, msg)

        return self.cleaned_data


class PessoaForm(forms.ModelForm):

    class Meta:

        model = Pessoa
        exclude = ['nome']
        

# Utilizado forms

'''
class PassagemForm(forms.Form):

    origem = forms.CharField(label='Origem', max_length=50)
    destino = forms.CharField(label='Destino', max_length=50)
    data_ida = forms.DateField(label='Ida', widget=DatePicker())
    data_volta = forms.DateField(label='Volta', widget=DatePicker())
    data_pesquisa = forms.DateField(label='Data da pesquisa', disabled=True, initial=datetime.today)
    classe_viagem = forms.ChoiceField(label='Classe do vôo', choices=tipos_de_classe)
    informacoes = forms.CharField(
        label='Informações adicionais',
        max_length=200,
        widget=forms.Textarea(),
        required=False
    )
    email = forms.EmailField(label='E-mail', max_length=100)

    def clean(self):

        origem = self.cleaned_data.get('origem')
        destino = self.cleaned_data.get('destino')
        data_ida = self.cleaned_data.get('data_ida')
        data_volta = self.cleaned_data.get('data_volta')
        data_pesquisa = self.cleaned_data.get('data_pesquisa')

        lista_erros = {}

        campo_tem_numero(origem, 'origem', lista_erros)
        campo_tem_numero(destino, 'destino', lista_erros)
        origem_destino_iguais(origem, destino, lista_erros)
        volta_menor_que_ida(data_ida, data_volta, lista_erros)
        ida_menor_que_hoje(data_ida, data_pesquisa, lista_erros)

        if lista_erros is not None:

            for erro in lista_erros:

                msg = lista_erros[erro]
                self.add_error(erro, msg)

        return self.cleaned_data
'''