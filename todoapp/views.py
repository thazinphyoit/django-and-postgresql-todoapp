from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def todo_list (request) :
    # return HttpResponse('Hello second time django test project!')
    return render(request, 'todoapp/todo_list.html')