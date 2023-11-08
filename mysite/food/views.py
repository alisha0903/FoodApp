from django.shortcuts import render, redirect 

from django.http import HttpResponse
from .models import *
from django.template import loader
from .forms import ItemForm
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView 
# # Create your views here. 

def index(request):
    item_list= Item.objects.all()
    template=loader.get_template('food/index.html')
    context={
       'item_list':item_list,
    }
    return render(request,'food/index.html')


def item (request):
    return HttpResponse('this is an item view')

def detail(request,item_id):
    item= Item.objects.get(pk=item_id)
    context={
       'item':item,
    }
    return render(request,'food/detail.html',context')

class FoodDetail(DetailView):
    mode=Item
    template_name='food/detail.html'

def create_item(request ):
    form = ItemForm(request.POST or None)

    if form.is_valid():
       form.save()
       return redirct('food:index')
    return render(request,'food/item-form.htmll',{'form:form'})

clas Create_item(CreateView):
    model  = tem;
    fields = ['item_name','item_desc','item_price','item_image']
    
    def form_valid(self,form):
       form.instance.username
    template_name = ".html"


def update_item(request,id):
    item=Item.objects.get(id=id)
    form=ItemForm(request.POST or None, instance=item)
    if form.valid():
        form.save()
        return redirect('food:index')
    return render(request,'food/item-form.html',{'form':form,'item':item})

def delete_item(request,id):
    item=Item.objects.get(id=id)

    if request.method == 'POST':
        item.delete()
        return redirect ('food:index')
    
    return render(request, 'food/item-delete.html',{'item':item})


    
