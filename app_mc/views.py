from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Despesas, Fechamentos, Faturamentos
from .forms import DespesasForm, FechamentosForm, FaturamentosForm
from django.db import connection
from datetime import datetime
from math import ceil

@login_required
def index(request):
    fechamentos = Fechamentos.objects.all()
    itens_carrosel = ceil(len(fechamentos)/3)

    lista = []
    grupo = []
    count = 0
    for item in fechamentos:
        grupo.append(item)
        count+=1
        if len(grupo) == 3:
            lista.append(grupo)
            grupo = []
    lista.append(grupo)

    return render(request, 'home.html', {'fechamentos':lista,'range':range(itens_carrosel)})

# CRUD DESPESAS
@login_required
def visualizarDespesas(request):
    despesas = Despesas.objects.all()
    return render(request, 'despesas/tabela_despesas.html',{'despesas':despesas})

@login_required
def criarDespesas(request):
    form = DespesasForm(request.POST or None)

    if form.is_valid():
        id_return_fechamento = form.cleaned_data['mes'].id
        form.save()
        return redirect('adm_fechamentos',id=id_return_fechamento)

    return render(request,'despesas/form_despesa.html', {'form':form})

@login_required
def atualizarDespesas(request, id):
    despesas = Despesas.objects.get(id=id)
    form = DespesasForm(request.POST or None, instance=despesas)

    if form.is_valid():
        id_return_fechamento = form.cleaned_data['mes'].id
        form.save()
        return redirect('adm_fechamentos',id=id_return_fechamento)

    return render(request, 'despesas/form_despesa.html', {'form':form,'despesas':despesas})

@login_required
def excluirDespesas(request, id):
    despesas = Despesas.objects.get(id=id)
    id_return_fechamento = Despesas.objects.get(id=id).mes_id

    if request.method == 'POST':
        despesas.delete()
        return redirect('adm_fechamentos',id=id_return_fechamento)

    return render(request, 'confirmar_remocao.html',{'parametro':despesas})
    
# CRUD FATURAMENTO
@login_required
def criarFaturamentos(request):
    form = FaturamentosForm(request.POST or None)

    if form.is_valid():
        id_return_fechamento = form.cleaned_data['mes'].id
        form.save()
        return redirect('adm_fechamentos',id=id_return_fechamento)

    return render(request,'faturamentos/form_faturamento.html', {'form':form})

@login_required
def atualizarFaturamentos(request, id):
    faturamentos = Faturamentos.objects.get(id=id)
    form = FaturamentosForm(request.POST or None, instance=faturamentos)

    if form.is_valid():
        id_return_fechamento = form.cleaned_data['mes'].id
        form.save()
        return redirect('adm_fechamentos',id=id_return_fechamento)

    return render(request, 'faturamentos/form_faturamento.html', {'form':form,'faturamentos':faturamentos})

@login_required
def excluirFaturamentos(request, id):
    faturamentos = Faturamentos.objects.get(id=id)
    id_return_fechamento = Faturamentos.objects.get(id=id).mes_id

    if request.method == 'POST':
        faturamentos.delete()
        cursor = connection.cursor()
        #cursor.execute('''SELECT * FROM app_mc_fechamentos WHERE MONTH(mes) = MONTH(DATE_FORMAT(NOW(), "%Y%m%d"))''')

        return redirect('adm_fechamentos',id=id_return_fechamento)

    return render(request, 'confirmar_remocao.html',{'parametro':faturamentos})

# Fechamento
@login_required
def criarFechamentos(request):
    form = FechamentosForm(request.POST or None)

    if form.is_valid():
        cursor = connection.cursor()
        
        form.instance.faturamento = 0
        form.instance.despesas = 0
        form.instance.balanco = 0

        # Verifica se o fechamento do mês já existe
        if cursor.execute('''SELECT * FROM app_mc_fechamentos WHERE MONTH(mes) = MONTH(DATE_FORMAT(NOW(), "%Y%m%d"))''') != 0:
            erro = "Você só pode ter um fechamento mensal, e o deste mês ({}) já foi criado.".format(traduz_mes(datetime.today().strftime("%m")))
            return render(request,'fechamentos/form_fechamento.html', {'form':form,'mes_atual':traduz_mes(datetime.today().strftime("%m")),'erro':erro})
        else:
            form.save()
        
        return redirect('criar_fechamentos')

    return render(request,'fechamentos/form_fechamento.html', {'form':form})

def admFechamentos(request,id):
    fechamentos = Fechamentos.objects.get(pk=id)
    despesas = Despesas.objects.filter(mes_id=id)
    faturamentos = Faturamentos.objects.filter(mes_id=id)

    return render(request,'fechamentos/tabela_fechamento.html',{'fechamentos':fechamentos,'despesas':despesas,'faturamentos':faturamentos})

# Função que traduz o mês
def traduz_mes(num):
    lista_meses = [None,'Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
    return lista_meses[int(num)]