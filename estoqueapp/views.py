from django.shortcuts import render, redirect
from estoqueapp.forms import ItensForm
from estoqueapp.models import Itens

def home(request):
    dados = {}
    search = request.GET.get('search')
    if search:
        dados['db'] = Itens.objects.filter(nome__icontains=search)
    else:
        dados['db'] = Itens.objects.all()
    return render(request, 'index.html', dados)

def form(request):
    dados={}
    dados['form'] = ItensForm()
    return render(request, 'form.html', dados)

def create(request):
    form = ItensForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def view(request, pk):
    data={}
    data['db'] = Itens.objects.get(pk=pk)
    return render(request, 'view.html', data)

def edit(request, pk):
    data={}
    data['db'] = Itens.objects.get(pk=pk)
    data['form'] = ItensForm(instance=data['db'])
    return render(request, 'form.html', data)
def update(request, pk):
    data = {}
    data['db'] = Itens.objects.get(pk=pk)
    form = ItensForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')

def delete(request, pk):
    db = Itens.objects.get(pk=pk)
    db.delete()
    return redirect(home)