from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import TodoApp

# Create your views here.
def todo_list (request) :
    # return HttpResponse('Hello second time django test project!')
    all_data = { 'todo_list' : TodoApp.objects.all()}
    return render(request, 'todoapp/todo_list.html', all_data)

def insert_todo (request: HttpRequest) :
    new_todo = TodoApp(content= request.POST['content'])
    new_todo.save()
    return redirect('/todo/list')

def delete_todo (request, todo_id) :
    delete_todo = TodoApp.objects.get(id=todo_id)
    delete_todo.delete()
    return redirect('/todo/list')
