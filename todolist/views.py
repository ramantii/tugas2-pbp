from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from todolist.models import Todolist
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse





# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    userid= request.user.id
    data = Todolist.objects.filter(pk = userid)
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


def update_task(request,id):
    task = Todolist.objects.get(pk=id )
    if task.isfinished :
        task.isfinished = False
    else:
        task.isfinished = True
    task.save()
    return redirect('todolist:show_todolist')

def delete(request,id):
    todolist = Todolist.objects.get(pk= id)
    todolist.delete()
    return redirect('todolist:show_todolist')