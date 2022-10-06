 
 ## Ramanti Prajna P.
 
Link deploy : https://task2pbp.herokuapp.com/todolist/login

# TUGAS 4
 # Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>? 
 The Cross-Site Request Forgery (CSRF) memaksa pengguna akhir untuk melakukan tindakan yang tidak diinginkan pada aplikasi web di mana mereka telah mengautentikasi diri mereka sendiri.Penyerang menggunakan status terotentikasi pengguna untuk keuntungan mereka dengan mengubah permintaan pengguna, yang mendorong pengguna untuk melakukan tindakan yang tidak ingin mereka lakukan. Jika serangan berhasil pada akun administratif, itu dapat membahayakan seluruh aplikasi web.CSRF adalah serangan umum, jadi Django memiliki implementasi yang sangat sederhana untuk meniadakan serangan ini. Django memiliki tag {% csrf_token %} yang diimplementasikan untuk menghindari serangan berbahaya. Kode ini menghasilkan token di sisi server saat merender halaman dan memastikan untuk memeriksa ulang token ini untuk setiap permintaan yang masuk kembali. Jika permintaan yang masuk tidak berisi token, permintaan tersebut tidak akan dieksekusi. Tag {% csrf_token %} dalam bahasa template Django disisipkan di dalam formulir. Dengan tambahan kode ini, serangan CSRF dapat dihindari, sehingga menjamin keamanan permintaan posting dari pengguna ke server. Tentunya dengan kata lain apabila kode {% csrf_token %} tidak disisipkan maka akan memungkinkan terjadinya CSRF. 

 # Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual. 
 Untuk membuat form secara manual maka perlu membuat forms dari Django 
 
 ### 1. Membuat file form.py dengan command
 
    from django import forms
    class NameForm(forms.Form):
        your_name = forms.CharField(label='Your name', max_length=100)
        
### 2. Membuat views.py

    from django.http import HttpResponseRedirect
    from django.shortcuts import render
    from .forms import NameForm
    def get_name(request):
        // if this is a POST request we need to process the form data
        if request.method == 'POST':
            // create a form instance and populate it with data from the request:
            form = NameForm(request.POST)
            // check whether it's valid:
            if form.is_valid():
                 process the data in form.cleaned_data as required
                * ...
                * redirect to a new URL:
                return HttpResponseRedirect('/thanks/')

        // if a GET (or any other method) we'll create a blank form
        else:
            form = NameForm()

        return render(request, 'name.html', {'form': form})
        
### 3. Membuat tampilan html misal nama.html
        <form action="/your-name/" method="post">
          {% csrf_token %}
          {{ form }}
         <input type="submit" value="Submit">
        </form>

 # Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML. 

  Dari tampilan awal user akan melakukan input data pada form, setelah tombol sumbit maka fungsi yang ada oada views.py mendapat input dari user di HTML dengan menggunakan perintah request.POST.get(). kemudian data akan di hubungkan ke models dan lanjut ke database dengan perintah (object),save(). Apabila user membuka data yang telah diinput mmaka data akan di tampilkan di file html dengan http request method "GET".


 # Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas. 
 

 1.  Membuat django-app bernama todolist dengan command python manage.py startapp todolist
 2.  Mendaftarkan aplikasi dengan menambah 'todolist' ke variabel INSTALLED_APPS 
 3.  Menambahkan routing dengan path('', include('todolist.urls')) pada urls.py di project_django 
 4.  Membuat models pada models.py sesuai yang dibutuhkan : Class Todolist dengan field user, date, title, description, dan isfinished
 5.  Mengimplementasikan form berupa form registrasi, fungsi login dan logout
 6.  Membuat html untuk tampilan todolist, login, logout, dan new_task
 7.  Migrasi skema model ke database Django lokal dengan command python manage.py makemigrations
 8.  Menerapkan skema yang di buat dalam database Django lokal dengan command python manage.py migrate 
 9.  Melakukan add, commit, dan push ke repositori GitHub dan deploy di Heroku dan membuat 2 akun dummy beserta 3 dummy data pada website hasil deployment

# TUGAS 5

# Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
-	CSS internal atau tertanam mengharuskan pengguna untuk menambahkan tag <style> di bagian <head> dokumen HTML Anda. Gaya CSS ini adalah metode yang efektif untuk menata satu halaman. Namun, menggunakan gaya ini untuk beberapa halaman memakan waktu karena pengguna perlu menempatkan aturan CSS di setiap halaman situs web pengguna.
Kelebihan dari CSS internal bisa menggunakan class dan ID selector. Kekurangannya menambah code ke htm doc akan meningkatkan page size dan loading time
-	Dengan CSS eksternal, pengguna akan menautkan halaman web pengguna ke file .css eksternal, yang dapat dibuat oleh editor teks apa pun di perangkat pegguna
Jenis CSS ini adalah metode yang lebih efisien, terutama untuk menata situs web besar. Dengan mengedit satu file .css, pengguna dapat mengubah seluruh situs sekaligus. Kelebihan CSS eksternal dapat menggunakan file .css yang sama untuk multiple pages. Kekurangan Halaman pengguna mungkin tidak dirender dengan benar sampai CSS eksternal dimuat 
-	CSS inline digunakan untuk menata elemen HTML tertentu. Untuk gaya CSS ini, pengguna hanya perlu menambahkan atribut gaya ke setiap tag HTML, tanpa menggunakan penyeleksi.
Jenis CSS ini sangat tidak disarankan, karena setiap tag HTML perlu ditata secara individual. Mengelola situs web pengguna mungkin menjadi terlalu sulit jika pengguna hanya menggunakan CSS inline. Kelebihannya dapat dengan mudah insert CSS rules ke html page. Kekuranganny Menambahkan CSS rules ke setiap elemen HTML memakan waktu dan membuat struktur HTML pengguna berantakan 

# Jelaskan tag HTML5 yang kamu ketahui.
* Tag html sebagai root, maksudnya semua tag yang berada didalam tag <HTML> merupakan gambaran dari dokumen HTML.
* Tag head untuk memberikan informasi tentang dokumen, maksudnya didalam tag <head> kita bisa menambahkan tag- tag yang biasanya digunakan untuk memberikan informasi berupa penulis, judul dokumen, kata kunci pada dokumen dan masih banyak lagi informasi yang bisa di tambahkan pada tag ini.
* Tag title untuk memberikan informasi berupa judul dokumen HTML.
* Tag body untuk memberikan isi dari suatu dokumen yang akan ditampilkan oleh web browsernya.
* Tag p untuk membuat sebuah paragraf.
* Tag komentar Untuk membuat komentar pada sebuah dokumen HTML, namun tulisan yang dimasukan dalam tag ini tidak akan terlihat pada Web browser saat dijalankan tetapi dapat dilihat pada source program.

# Jelaskan tipe-tipe CSS selector yang kamu ketahui.
* .class  select element dengan class =”class”
* #id  select element dengan id =”id”
* :active  select link aktif
* Element select all <element> 

# Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1.	Memasang bootstrap pada base.html
2.	Melakukan modifikasi styling pada registrasi.html , login.html, new_task.html, todolist.html


