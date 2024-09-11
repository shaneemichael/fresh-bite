Berikut langkah-langkah yang perlu dilakukan:

1) **Membuat Proyek Django Baru:**
   - Buat direktori lokal bernama `fresh-bite` lalu aktifkan virtual environment di dalam direktori tersebut.
   - Buat file `requirements.txt` yang berisi dependencies, dan install dependencies tersebut. Setelah itu, jalankan perintah `django-admin startproject fresh_bite .`, yang akan menghasilkan direktori `fresh-bite` dengan konfigurasi dasar untuk proyek Django.
   - Tambahkan `localhost` ke dalam ALLOWED_HOSTS di `settings.py`, lalu jalankan server Django pada direktori lokal.
   - Buat repositori GitHub dengan nama `fresh-bite`. Setelah itu, inisialisasi direktori lokal `fresh-bite` sebagai repositori Git.
   - Tambahkan file `.gitignore` untuk mengabaikan file yang tidak perlu, kemudian push semua perubahan dari repositori lokal ke repositori GitHub.

2) **Membuat Aplikasi Baru Bernama "main":**
   - Buat aplikasi baru bernama `main` dalam proyek `fresh_bite` dengan menjalankan perintah `python manage.py startapp main`, yang akan membuat folder `main` berisi file dasar Django seperti `views.py`, `models.py`, dan `urls.py`.
   - Tambahkan aplikasi `main` ke dalam daftar `INSTALLED_APPS` di `settings.py`, agar Django mengenali aplikasi baru tersebut.

3) **Routing Proyek untuk Menjalankan Aplikasi "main":**
   - Import fungsi `include` dari `django.urls`.
   - Tambahkan URL `path('', include('main.urls'))` ke variabel `urlpatterns`, sehingga URL root akan diarahkan ke aplikasi `main`.

4) **Membuat Model "product" di Aplikasi "main" (fresh_bite):**
   - Pada file `models.py` dalam aplikasi `main`, buat model bernama `Product` dengan tiga atribut: `name` (CharField), `price` (IntegerField), dan `description` (TextField).

5) **Membuat Fungsi di `views.py` untuk Ditampilkan di Template HTML:**
   - Buka `views.py` dalam aplikasi `main` dan import `render` dari `django.shortcuts`.
   - Tambahkan fungsi `show_main` yang memuat context data.
   - Return fungsi dengan `render(request, "main.html", context)` untuk menampilkan template `main.html` dengan data dari context.
   - Edit `main.html` untuk menampilkan nama aplikasi dan detail nama serta kelas menggunakan template variables Django.

6) **Membuat Routing di `urls.py` untuk Memetakan Fungsi di `views.py`:**
   - Untuk memetakan URL ke fungsi di `views.py`, tambahkan path pada `urls.py`. Contohnya, `path('', views.home, name='home')` akan memetakan URL root ke fungsi `home` di `views.py`, sehingga fungsi tersebut akan dipanggil ketika URL diakses.

7) **Melakukan Deployment ke PWS:**
   - Buat proyek baru di PWS, kemudian tambahkan URL deployment `shane-michael-freshbite2go.pbp.cs.ui.ac.id` ke dalam ALLOWED_HOSTS di `settings.py`, sesuai dengan username dan nama proyek.
   - Jalankan perintah untuk mempush perubahan ke PWS, ganti branch menjadi `main`.
   - Push perubahan dari repositori lokal ke PWS dengan perintah `git push pws main:master`.

8) **Membuat File README.md:**
   - Buat file README.md di direktori utama proyek.
   - Tambahkan informasi dan keterangan proyek yang diperlukan ke dalam README.md.

Setelah semua langkah selesai, lakukan git add, commit, dan push ke GitHub serta PWS. Jangan lupa untuk mematikan virtual environment setelah pekerjaan selesai.


Fungsi Git:
1) Melacak perubahan kode
   - Git memungkinkan untuk menyimpan riawayat perubahan pada kode, sehingga setiap versi atau modifikasi dapat diketahui kapan perubahannya, apa perubahannya, dan siapa yang melakukan perubahan.
2) Kolaborasi tim
   - Git memudahkan kolaborasi antar pengembang, terutama dalam proyek besar. Dengan fitur branching dan merging, banyak pengembang dapat bekerja pada fitur atau bagian kode yang berbeda secara paralel, tanpa mengganggu kode di cabang utama (main branch).
3) Membantu dalam pemulihan kode
   - Karena semua perubahan tercatat, pengembang bisa dengan mudah rollback atau kembali ke versi kode sebelumnya jika ada masalah atau bug yang muncul akibat perubahan baru.
4) Menyelesaikan konflik kode
   - Git membantu dalam mengelola dan menyelesaikan konflik kode yang terjadi ketika beberapa pengembang melakukan perubahan pada bagian yang sama dari sebuah file.
5) Integrasi dengan Alat CI/CD
   - Git sering digunakan bersama dengan alat Continuous Integration (CI) dan Continuous Deployment (CD) untuk mengotomatisasi proses pengujian dan deployment. Setiap kali kode di-push ke repositori, tes otomatis dapat dijalankan dan aplikasi bisa langsung di-deploy.


Mengapa Django?
1) Open source:
   - Django adalah framework open source, yang berarti siapa saja bisa menggunakannya secara gratis. Ini didukung oleh komunitas yang besar dan aktif, yang terus memperbarui dan meningkatkan Django. Banyak dokumentasi, tutorial, dan paket tambahan tersedia secara bebas.

2) Ridiculously fast:
   - Django dirancang untuk membantu pengembang membangun aplikasi dengan cepat. Django menangani banyak detail pengembangan web (seperti routing, form handling, validasi, autentikasi) secara otomatis, memungkinkan pengembang untuk fokus pada logika inti aplikasi. Dengan pendekatan "batteries included", Django menawarkan banyak fitur bawaan sehingga aplikasi dapat dikembangkan dengan sangat cepat.
3) 