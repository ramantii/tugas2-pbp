
from todolist.views import delete, register #sesuaikan dengan nama fungsi yang dibuat
from todolist.views import login_user
from todolist.views import logout_user
from todolist.views import create_task
from todolist.views import show_todolist
# from todolist.views import finished
# from todolist.views import unfinished
from todolist.views import update_task
from todolist.views import delete
from django.urls import path

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),  
    path('login/',login_user, name='login'),
    path('logout/',logout_user, name='logout'),
    path('create-task/', create_task, name='create-task'),
    path('update-task/<int:id>/',update_task,name='update-task'),
    # path('finished/<int:id>/',finished, name='finished'),
    # path('unfinished/<int:id>/',unfinished, name='unfinished'),
    path('delete-todolist/<int:id>/',delete,name='delete-todolist'),

]
