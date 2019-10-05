from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from rest_framework import viewsets
from .serializers import ContentSerializer, ContentMiniSerializer

from django.template import RequestContext
from .forms import ContentForm
from .models import Content
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

@method_decorator(csrf_exempt, name='dispatch')
class ContentViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer

    def list(self, request, *args, **kwargs):
        contents = Content.objects.all()
        serializer = ContentMiniSerializer(contents, many=True)
        return Response(serializer.data)



def content_create_view(request):
    form = ContentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/content/')
    context = {
        'form': form
    }
    return render(request, "content/content_create.html", context)


# def content_update_view(request, id):
#
#     obj = get_object_or_404(Content, id=id)
#     print(obj)
#     form = ContentForm(request.POST or None, instance=obj)
#     print(form)
#     if form.is_valid():
#         form.save()
#     context = {
#         'form': form
#     }
#     return render(request, "content/content_create.html", context)

def content_list_view(request):
    queryset = Content.objects.all()

    context = {
        "object_list": queryset
    }

    return render(request, "content/content_list.html", context)
