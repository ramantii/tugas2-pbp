# TUGAS 6

## perbedaan antara asynchronous programming dengan synchronous programming
**synchronous programming**, membuat request dengan mengeksekusi program satu-persatu pada baris secara hirarki dan disesuaikan dengan prioritas dari request tersebut. Tentunya dengan hal tersebut membuat eksekusi program menjadi lama karena request harus menunggu request lain untuk selesai lebih dahulu. 

**asynchronous programming**, program dapat berjalan secara bersamaan (multi-thread), non-blocking yang artinya dapat mengirim multiple request ke server

## paradigma Event-Driven Programming
Meripakan paradigma suatu code dibuat untuk merespon suatu kejadian. digunakan untuk menyinkronkan terjadinya beberapa peristiwa dan membuat program sesederhana mungkin. Komponen dasar dari Event-Driven Proramming adalah:

* Fungsi callback ( disebut event handler) dipanggil saat event dipicu.
* Loop peristiwa yang mendengarkan pemicu peristiwa dan memanggil pengendali peristiwa yang sesuai untuk peristiwa itu.

## penerapan asynchronous programming pada AJAX

AJAX dapat digunakan untuk mengirim dan mengambil data dari server secara asynchronous. Salah satu contoh penerapannya adalah ketika tombol submit ditekan, maka JavaScript AJAX akan mengirimkan sebuah request ke server. Setelah itu server akan memproses request dan mengembalikan response ke web dan nantinya akan dibaca oleh JavaScript.

## cara mengimplementasikan checklist 

AJAX GET
1. Membuat view baru untuk mengembalikan data dalam bentuk json
2. Membuat path urls untuk mengarah ke view
3. Menggunakan AJAX GET 

AJAX POST
1. Membuat add task untuk membuka modal 
2. Membuat view untuk menambahkan task 
3. Membuat path yang mengarah ke view
4. Menerapkan AJAX POST