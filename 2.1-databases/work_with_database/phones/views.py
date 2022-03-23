from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort')
    if sort == 'name':
        item = Phone.objects.all().order_by('name')
    elif sort == 'min_price':
        item = Phone.objects.all().order_by('price')
    elif sort == 'max_price':
        item = Phone.objects.all().order_by('-price')
    else:
        item = Phone.objects.all()
    context = {
        'phones': item
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {
        'phone': Phone.objects.get(slug=slug)
    }
    return render(request, template, context)
