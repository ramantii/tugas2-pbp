 # Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>? 
 The Cross-Site Request Forgery (CSRF) memaksa pengguna akhir untuk melakukan tindakan yang tidak diinginkan pada aplikasi web di mana mereka telah mengautentikasi diri mereka sendiri.Penyerang menggunakan status terotentikasi pengguna untuk keuntungan mereka dengan mengubah permintaan pengguna, yang mendorong pengguna untuk melakukan tindakan yang tidak ingin mereka lakukan. Jika serangan berhasil pada akun administratif, itu dapat membahayakan seluruh aplikasi web.CSRF adalah serangan umum, jadi Django memiliki implementasi yang sangat sederhana untuk meniadakan serangan ini. Django memiliki tag {% csrf_token %} yang diimplementasikan untuk menghindari serangan berbahaya. Kode ini menghasilkan token di sisi server saat merender halaman dan memastikan untuk memeriksa ulang token ini untuk setiap permintaan yang masuk kembali. Jika permintaan yang masuk tidak berisi token, permintaan tersebut tidak akan dieksekusi. Tag {% csrf_token %} dalam bahasa template Django disisipkan di dalam formulir. Dengan tambahan kode ini, serangan CSRF dapat dihindari, sehingga menjamin keamanan permintaan posting dari pengguna ke server. Tentunya dengan kata lain apabila kode {% csrf_token %} tidak disisipkan maka akan memungkinkan terjadinya CSRF. 

 # Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual. 
 
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
 9.  Melakukan add, commit, dan push ke  ke repositori GitHub dan deploy di Heroku dan membuat 2 akun dummy beserta 3 dummy data pada website hasil deployment



