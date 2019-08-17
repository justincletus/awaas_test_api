from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Product
from .forms import ProductForm


# Create your views here.
def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
        return redirect('../')
    
    context = {
        'form': form
    }

    return render(request, 'products/product_create.html', context)

# Create your views here.
def product_update_view(request, id):
    obj = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('../../')
    
    context = {
        'form': form
    }

    return render(request, 'products/product_create.html', context)

def product_list_view(request):
    queryset = Product.objects.all()

    context = {
        'object_list': queryset
    }

    return render(request, "products/product_list.html", context)

def product_detail_view(request, id):
    try:
        obj = Product.objects.get(id=id)
    except:
        raise Http404
    
    result = {
        "object": obj
    }   

    return render(request, "products/product_detail.html", result)

def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    
    result = {
        "object": obj
    }

    return render(request, 'products/product_delete.html', result)


