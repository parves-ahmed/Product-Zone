from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm

# Create your views here.


def index(request):
    return render(request, 'product/index.html')


def create_item(request):
    form = ProductForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('details')

    return render(request, 'product/create_item.html', {'form': form})


def details_item(request):
    products = Product.objects.all()
    return render(request, 'product/product_list.html', {'products': products})


def update_item(request, id):
    product = Product.objects.get(id=id)
    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid():
        form.save()
        return redirect('details')

    return render(request, 'product/create_item.html', {'form': form, 'product': product})


def delete_item(request, id):
    product = Product.objects.get(id=id)

    if request.method == 'POST':
        product.delete()
        return redirect('details')

    return render(request, 'product/delete_confirm.html', {'product': product})