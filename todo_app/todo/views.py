from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import todoitem

# Create your views here.

def welcome(request):
    return render(request,'todo/welcome.html')

def home(request):
    if request.method == "POST":
        new_todo_item = todoitem(item = request.POST["content"])
        new_todo_item.save()
        return HttpResponseRedirect("/home/")
    else:
        pass
    all_todo_items = todoitem.objects.all()
    return render(request, 'todo/home.html', {"all_items": all_todo_items})

def deletetodo(request, todo_id):
    item_to_delete = todoitem.objects.get(id=todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect("/home/")

def updatetodo(request, todo_id):
    if request.method == "POST":
        currentitem = todoitem.objects.get(id=todo_id)
        currentitem.item = request.POST["UpdatedItem"]
        currentitem.save()
        return HttpResponseRedirect("/home/")
    
def about_page(request):
    return render(request, 'todo/about.html')

