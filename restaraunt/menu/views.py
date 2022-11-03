from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .models import menuItem


def index(request, myMenu=None):
    myMenu = menuItem.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'myMenu': myMenu,
    }
    return HttpResponse(template.render(context, request))


def addItem(request):
    template = loader.get_template("addItem.html")
    return HttpResponse(template.render({}, request))


def addItemSubmit(request):
    category = request.POST['category']
    price = request.POST['price']
    name = request.POST['name']
    item = menuItem(category=category, price=price, name=name)
    item.save()
    return HttpResponseRedirect(reverse('index'))


def deleteItem(request, id):
    item = menuItem.objects.get(id=id)
    item.delete()
    return HttpResponseRedirect(reverse('index'))


def updateItem(request, id):
    myItem = menuItem.objects.get(id=id)
    template = loader.get_template('updateItem.html')
    context = {
        'myItem': myItem,
    }
    return HttpResponse(template.render(context, request))


def updateItemSubmit(request, id):
    category = request.POST['category']
    price = request.POST['price']
    name = request.POST['name']
    item = menuItem.objects.get(id=id)
    item.category = category
    item.price = price
    item.name = name
    item.save()
    return HttpResponseRedirect(reverse('index'))

