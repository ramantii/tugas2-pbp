from todolist.views import register #sesuaikan dengan nama fungsi yang dibuat
from todolist.views import login_user
from todolist.views import logout_user
from django.urls import path

app_name = 'todolist'

urlpatterns = [
    # path('', show_todolist, name='show_todolist')
    path('register/', register, name='register'),  
    path('login_user/',login_user, name='login'),
    path('logout_user/',logout_user, name='logout'),
]
