from django.http import Http404
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404

from .models import Good
# Create your views here.

class GoodListView(ListView):
    queryset = Good.objects.all()
    template_name = "goods/list.html"

    # def get_context_data(self, *args, **kwargs):
        # context = super(GoodListView, self).get_context_data(*args, **kwargs)
        # print(context)
        # return context

    def get_queryset(self, *args, **kwargs):
        request = self. request
        return Good.objects.all()

def good_list_view(request):
    queryset = Good.objects.all()
    context = {
            'object_list' : queryset
    }
    return render(request, "goods/list.html", context)

class GoodDetailView(DetailView):
    #queryset = Good.objects.all()
    template_name = "goods/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(GoodDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        return context
    
    def get_object(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        instance = Good.objects.get_by_id(pk)
        if instance is None:
            raise Http404("Good doesn't exist.")
        return instance

    # def get_queryset(self, *args, **kwargs):
        # request = self.request
        # pk = self.kwargs.get('pk')
        # return Good.objects.filter(pk=pk)

def good_detail_view(request, pk=None, *args, **kwargs):
    #instance  = get_object_or_404(Good, pk=pk)
    # try:

        # instance = Good.objects.get(id=pk)
    # except Good.DoesNotExist:
        # print('no product here')
        # raise Http404("Good doesn't exist.")
    # except:
        # print("huh?")
    instance = Good.objects.get_by_id(pk)
    if instance is None:
        raise Http404("Good doesn't exist.")
    #print(instance)
    # qs = Good.objects.filter(id=pk)
    
    # if qs.exists() and qs.count() == 1:
        # instance = qs.first()
    # else:
        # raise Http404("Good doesn't exist.")

    
    context = {
            'object' : instance
    }
    return render(request, "goods/detail.html", context)
