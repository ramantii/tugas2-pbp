# **link deploy** 

**apps** :

html :
json :
xml :



# **Perbedaan xml, json dan html**
|XML|JSON|HTML|
|---|---|---|
|Mendukung berbagai encoding|Hanya mendukung encoding UTF-8 saja|Mendukung berbagai encoding|
|Mendukung comment|Tidak mendukung comment|Mendukung comment|
|Berbasis markup language|Berbasis bahasa JavaScript|Berbasis markup language|
|Tidak mendukung data type array|Dapat menyimpan data dalam bentuk array dan menjadikan transfer data menjadi lebih mudah|Dapat memunculkan pemetaan data dari sebuah array |
|Mendukung namespaces|Tidak mendukung namespaces|Tidak mendukung namespaces|
|Syntax xml ada start dan end tag|Syntax json lebih ringan dan ada start dan end tag|Syntax html ada start dan end tag|


# **Mengapa perlu data delivery dalam pengimplementasian sebuah platform?**

Data delivery dibutuhkan untuk mengintegrasikan antara frontend dan backend. Tentu dalam pengintegrasian tersebut dibutuhkan suatu perantara. Perantara yang digunakan dalam hal ini adalah json, xml atau html. Melakukan data delivery juga akan mempermudah dalam mengirimkan data yang ada di server. Dengan demikian data yang dideliver bisa diterima oleh user dan cenderung mudah untuk melakukan development. 

# **Implementasi**

1.	Membuat aplikasi 'mywatchlist'  dengan command  python manage.py startapp mywatchlist
2.	Melakukan route url dengan menambahkan path pada urls.py pada urlpatterns dengan path('mywatchlist/', include('mywatchlist.urls')) , menambah path ke dalam /project_django/urls.py lalu juga path
path('', show_html, name='show_watchlist') ke dalam /mywatchlist/urls.py, serta menambahkan mywatchlist pada installed_app yang ada di setting.py .
3.	Membuat model pada model.py
class MyWatchList(models.Model):
    watched = models.BooleanField()
    title = models.TextField()
    rating = models.IntegerField()
    release_date = models.DateField()
    review = models.TextField()
selanjutnya lakukan migrasi dan load data. 

# **Screenshoot postman**
![Screenshot (319)](https://user-images.githubusercontent.com/110367908/191539038-4f02cbbf-c1bc-4551-a117-bcf949b1dac8.png)
![Screenshot (320)](https://user-images.githubusercontent.com/110367908/191539122-3d9f519a-0fe8-4f47-ba6c-94e2fbfe1218.png)
![Screenshot (321)](https://user-images.githubusercontent.com/110367908/191539146-b48ef678-8939-4f5f-9f35-bebbc01d25cc.png)
