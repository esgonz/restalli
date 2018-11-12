from django.shortcuts import render, HttpResponse, redirect
from .models import stock
# Create your views here.

def index(request):
    stocks = stock.objects.all()
    context = {
        'stocks': stocks
    }
    return render(request, 'index.html', context)

def crear(request):
    print(request.POST)
    title = request.GET['title']
    slugstock = request.GET['slugstock']
    categoria = request.GET['categoria']
    porciones = request.GET['porciones']
    cantidad = request.GET['cantidad']
    price = request.GET['price']
    status = request.GET['status']
    stock_details = stock(title=title,slugstock=slugstock,categoria=categoria, porciones=porciones, cantidad=cantidad, price=price, status=status)
    stock_details.save()
    return redirect('/')

def agregar_stock(request):
    return render(request, 'agregar_stock.html')



def eliminar(request, id):
    stocks = stock.objects.get(pk=id)
    stocks.delete()
    return redirect('/')

def editar(request, id):
    stocks = stock.objects.get(pk=id)
    context = {
        'stocks': stocks
    }
    return render(request, 'editar.html', context)


def modificar(request, id):
    stocks = stock.objects.get(pk=id)
    title = request.GET['title']
    slugstock = request.GET['slugstock']
    categoria = request.GET['categoria']
    porciones = request.GET['porciones']
    cantidad = request.GET['cantidad']
    price = request.GET['price']
    status = request.GET['status']
    stocks.save()
    return redirect('/')
