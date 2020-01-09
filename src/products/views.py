from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Product
from .forms import ProductForm


# Create product view.
def product_create_view(request):
    form = ProductForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        image = request.POST.get('product_image')
        form.save()
        form = ProductForm()
        return redirect('../')

    context = {
        'form': form
    }

    return render(request, 'products/product_create.html', context)

# Update product view.
def product_update_view(request, slug):
    obj = get_object_or_404(Product, slug=slug)
    form = ProductForm(request.POST or None, request.FILES or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('../../')

    context = {
        'form': form
    }

    return render(request, 'products/product_create.html', context)

# List all products
def product_list_view(request):
    queryset = Product.objects.all()

    context = {
        'object_list': queryset
    }

    return render(request, "products/product_list.html", context)

# show specific product detail
def product_detail_view(request, slug):
    try:
        obj = Product.objects.get(slug=slug)
    except:
        raise Http404

    result = {
        "object": obj
    }

    return render(request, "products/product_detail.html", result)

# delete product
def product_delete_view(request, slug):
    obj = get_object_or_404(Product, slug=slug)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')

    result = {
        "object": obj
    }

    return render(request, 'products/product_delete.html', result)
