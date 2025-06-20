from django.shortcuts import render, redirect
from django.http import HttpResponse

from lists.models import Item, List


def home_page(request):
    return render(request, "home.html")


def view_list(request, list_id):
    list_items = List.objects.get(id=list_id)
    return render(request, "list.html", {"list": list_items})


def new_list(request):
    list_items = List.objects.create()
    Item.objects.create(text=request.POST["item_text"], list=list_items)
    return redirect(f"/lists/{list_items.id}/")


def add_item(request, list_id):
    list_items = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST["item_text"], list=list_items)
    return redirect(f"/lists/{list_items.id}/")
