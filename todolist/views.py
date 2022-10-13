from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from todolist.models import Todolist
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.core import serializers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt



# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data = Todolist.objects.filter(user=request.user)
    username = request.user.username
    context = {
        'name' : username,
        'last_login': request.COOKIES['last_login'],
        'todolists': data
    }
    return render(request, "todolist.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

def create_task(request):
    if request.method == "POST":
        user = request.user
        date = request.POST.get("date")
        title = request.POST.get("title")
        description = request.POST.get("description")
        create_task = Todolist(user=user,date=date, title=title, description=description)
        create_task.save()
        return redirect('todolist:show_todolist')

    return render(request, "new_task.html")

@csrf_exempt
def update_task(request,id):
    item = Todolist.objects.get(pk=id)
    finished = not item.isfinished
    item.isfinished = finished
    item.save()
    return JsonResponse({"isfinished": finished})

@csrf_exempt
def delete(request,id):
    todolist = Todolist.objects.get(pk= id)
    todolist.delete()
    return redirect('todolist:show_todolist')

@login_required(login_url='/todolist/login/')
def get_todolist_json(request):
    todolist_item = Todolist.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", todolist_item),content_type="application/json")

@login_required(login_url='/todolist/login/')
@csrf_exempt
def add_todolist_item(request):
    if request.method == "POST":
        user=request.user
        title = request.POST.get("title")
        description = request.POST.get("description")

        new_todolist = Todolist(user=user,title=title,description=description)
        new_todolist.save()

    return JsonResponse({"pk": new_todolist.pk, "fields":{"title":new_todolist.title,"description": new_todolist.description,"isfinished": new_todolist.isfinished}})



    