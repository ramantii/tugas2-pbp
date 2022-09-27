link apps :   https://task2pbp.herokuapp.com/katalog/

![Screenshot 2022-09-14 203539](https://user-images.githubusercontent.com/110367908/190168930-f13b0a34-6f48-4be8-acca-8222b6644665.jpg)
# DEFINISI #



URL: Meskipun dimungkinkan untuk memproses permintaan dari setiap URL melalui satu fungsi, jauh lebih mudah untuk menulis fungsi tampilan terpisah untuk menangani setiap sumber daya. URL mapper digunakan untuk mengarahkan HTTP  request ke tampilan yang sesuai berdasarkan URL request. URL mapper juga dapat mencocokkan pola string atau angka tertentu yang muncul di URL dan meneruskannya ke fungsi tampilan sebagai data.
view: view adalah fungsi pengendali request, yang menerima HTTP request dan mengembalikan respons HTTP. View mengakses data yang diperlukan untuk memenuhi permintaan melalui model, dan mendelegasikan pemformatan respons ke template.
Model: Model adalah objek Python yang mendefinisikan struktur data aplikasi, dan menyediakan mekanisme untuk mengelola (menambah, memodifikasi, menghapus) dan meminta catatan dalam database.
Template: Template adalah file teks yang mendefinisikan struktur atau tata letak file (seperti halaman HTML), dengan tempat penampung yang digunakan untuk mewakili konten aktual. Tampilan dapat secara dinamis membuat halaman HTML menggunakan template HTML, mengisinya dengan data dari model. Sebuah template dapat digunakan untuk mendefinisikan struktur dari semua jenis file; tidak harus HTML

1.	Mengirim request ke right view (urls.py)
URL mapper biasanya disimpan dalam file bernama urls.py. Pada contoh di bawah ini, mapper (urlpatterns) mendefinisikan daftar pemetaan antara rute (pola URL tertentu) dan fungsi tampilan yang sesuai. Jika Permintaan HTTP diterima yang memiliki URL yang cocok dengan pola tertentu, maka fungsi tampilan terkait akan dipanggil dan meneruskan permintaan tersebut.

![1](https://user-images.githubusercontent.com/110367908/190167821-b8c9db82-1a61-4348-b58f-afbddeb2b3ae.png)

2.	Handle request (view.py)
Tampilan adalah inti dari aplikasi web, menerima permintaan HTTP dari klien web dan mengembalikan tanggapan HTTP. Di antaranya, mereka menyusun sumber daya lain dari kerangka kerja untuk mengakses database, membuat template, dll.

![2](https://user-images.githubusercontent.com/110367908/190167937-81924460-8d78-41ff-85d0-e7bd0e43dcb6.png)

3.	Mendefinisikan data model (models.py)
Aplikasi web Django mengelola dan meminta data melalui objek Python yang disebut sebagai model. Model menentukan struktur data yang disimpan, termasuk jenis bidang dan mungkin juga ukuran maksimumnya, nilai default, opsi daftar pilihan, teks bantuan untuk dokumentasi, teks label untuk formulir, dll. Definisi model tidak bergantung pada database yang mendasarinya — Anda dapat memilih salah satu dari beberapa sebagai bagian dari pengaturan proyek Anda. 

![3](https://user-images.githubusercontent.com/110367908/190168165-5692e45f-2ba1-4115-aae8-bdca8d58a032.png)

4.	Meminta/mengirimkan  data (views.py)
Model Django menyediakan API kueri sederhana untuk mencari database terkait. 
data_item_catalog = CatalogItem.object.all()  bagaimana kita dapat menggunakan API kueri 
Fungsi ini menggunakan fungsi render() untuk membuat HttpResponse yang dikirim kembali ke browser. Fungsi ini adalah jalan pintas; itu membuat file HTML dengan menggabungkan template HTML tertentu dan beberapa data untuk dimasukkan ke dalam template.

![4](https://user-images.githubusercontent.com/110367908/190168271-0918cfa0-8017-4bb4-9a93-2b1068edd251.png)

5.	Rendering data (HTML templates)
Sistem template memungkinkan Anda menentukan struktur dokumen keluaran untuk data yang akan diisi saat halaman dibuat. Template sering digunakan untuk membuat HTML, tetapi juga dapat membuat jenis dokumen lainnya. Ini merupakan base.html pada aplikasi katalog

![5](https://user-images.githubusercontent.com/110367908/190168364-87bc7943-aa63-4d7c-b136-3583aba026fa.png)

# Mengapa perlu Virtual Environment? #
Dalam menjalankan sistem,  virtual environment diperlukan agar berjalan di lingkungan terisolasi. Tujuan dari virtual environtment juga berguna untuk maintain dependensi project yang berbeda-beda. Dengan demikian juga tujuan dari melakukan virtual environment pada sistem bertujuan untuk menghindari error yang memungkinkan. Sehingga dapat disimpulkan bahwa virtual environment diperlukan untuk menghindri permasalahan yang memungkinkan terjadi dalam proses pengembangan. 


# Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual Environtment ? #

Bisa, dalam kondisi hanya pada lingkungan local server. Namun demikian tidak menggunakan virtual environment juga akan memungkinkan potensi yang terjadi seperti error ataupun kesalahan lain yang bisa menghambat pengembang. Kesimpulannya kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual Environtment.

# Mengapa perlu Virtual Environment? #
Dalam menjalankan sistem,  virtual environment diperlukan agar berjalan di lingkungan terisolasi. Tujuan dari virtual environtment juga berguna untuk maintain dependensi project yang berbeda-beda. Dengan demikian juga tujuan dari melakukan virtual environment pada sistem bertujuan untuk menghindari error yang memungkinkan. Sehingga dapat disimpulkan bahwa virtual environment diperlukan untuk menghindri permasalahan yang memungkinkan terjadi dalam proses pengembangan. 


# Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual Environtment ? #

Bisa, dalam kondisi hanya pada lingkungan local server. Namun demikian tidak menggunakan virtual environment juga akan memungkinkan potensi yang terjadi seperti error ataupun kesalahan lain yang bisa menghambat pengembang. Kesimpulannya kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual Environtment.


