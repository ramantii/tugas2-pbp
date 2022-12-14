
from todolist.views import delete, register #sesuaikan dengan nama fungsi yang dibuat
from todolist.views import login_user
from todolist.views import logout_user
from todolist.views import create_task
from todolist.views import show_todolist
from todolist.views import update_task
from todolist.views import delete
from todolist.views import add_todolist_item
from todolist.views import get_todolist_json
from django.urls import path

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),  
    path('login/',login_user, name='login'),
    path('logout/',logout_user, name='logout'),
    path('create-task/', create_task, name='create-task'),
    path('update-task/<int:id>/',update_task,name='update-task'),
    path('delete-todolist/<int:id>/',delete,name='delete-todolist'),
    path('json/', get_todolist_json,name='get-todolist-json'),
    path('add/',add_todolist_item,name='add-todolist-item')

]
