from django.urls import path
from mywatchlist.views import show_mywatchlist
from mywatchlist.views import show_xml
from mywatchlist.views import show_json
from mywatchlist.views import show_html

app_name = 'mywatchlist2'

urlpatterns = [
    path('', show_mywatchlist, name='show_mywatchlist2'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('html/', show_html ,name='show_html'),
]