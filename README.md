#### Link PWS: http:// ####
# Tugas Individu 2 #
#### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).####

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

#### Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara `urls.py`, `views.py`, `models.py`, dan berkas `html`.####

![Bagan Django](https://github.com/shaneemichael/fresh-bite/blob/main/components/bagan_django.jpeg)

Penjelasan:
Permintaan dari klien pertama kali diproses oleh urls.py, yang akan mencocokkan URL tersebut dengan fungsi view yang tepat di views.py. Di dalam views.py, logika aplikasi dijalankan dan jika diperlukan data dari database, fungsi view akan memanggil model yang ada di models.py. Setelah data diambil, view akan menyiapkan template HTML dengan data tersebut dan merendernya. Akhirnya, halaman web atau respons JSON dikirim kembali ke browser klien.

#### Jelaskan fungsi git dalam pengembangan perangkat lunak!####

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


#### Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak? ####

1) Open source:
   - Django adalah framework open source, yang berarti siapa saja bisa menggunakannya secara gratis. Ini didukung oleh komunitas yang besar dan aktif, yang terus memperbarui dan meningkatkan Django. Banyak dokumentasi, tutorial, dan paket tambahan tersedia secara bebas.
2) Ridiculously fast:
   - Django dirancang untuk membantu pengembang membangun aplikasi dengan cepat. Django menangani banyak detail pengembangan web (seperti routing, form handling, validasi, autentikasi) secara otomatis, memungkinkan pengembang untuk fokus pada logika inti aplikasi. Dengan pendekatan "batteries included", Django menawarkan banyak fitur bawaan sehingga aplikasi dapat dikembangkan dengan sangat cepat.
3) Fully Loaded:
   - Django hadir dengan banyak fitur bawaan yang meliputi sistem autentikasi pengguna, admin panel, routing URL, manajemen file statis (gambar, CSS, JavaScript), Sistem ORM (Object-Relational Mapping) untuk berinteraksi dengan database Dengan fitur bawaan yang lengkap ini, pengembang tidak perlu mengandalkan banyak alat eksternal, sehingga lebih mudah dalam manajemen proyek.
4) Reassuringly Secure:
   - Django memiliki fokus yang kuat pada keamanan. Ini secara otomatis menangani masalah keamanan umum seperti Cross-Site Scripting (XSS), Cross-Site Request Forgery (CSRF), SQL Injection, Clickjacking Django juga mendorong penggunaan praktik keamanan terbaik, seperti hashing kata sandi dan sistem manajemen izin pengguna yang baik.
5) Exceedingly Scalable:
   - Django dirancang agar bisa di-scale untuk menangani aplikasi dengan trafik yang sangat tinggi. Banyak situs besar seperti Instagram dan Pinterest menggunakan Django karena skalabilitasnya. Django dapat diintegrasikan dengan berbagai komponen backend seperti database SQL, NoSQL, cache, dan sistem load balancing, sehingga memungkinkan aplikasi untuk tumbuh sesuai kebutuhan.
6) Incredibly Versatile:
   - Django sangat fleksibel dan bisa digunakan untuk berbagai jenis aplikasi web, seperti situs web konten, aplikasi e-commerce, platform sosial API backend (REST dan GraphQL) Django juga mendukung integrasi dengan berbagai teknologi seperti REST API, WebSockets, atau GraphQL, sehingga bisa digunakan untuk berbagai keperluan pengembangan.

#### Mengapa model pada Django disebut sebagai ORM? ####

Model pada Django disebut sebagai ORM (Object-Relational Mapping) karena berfungsi sebagai jembatan antara objek dalam kode Python dan data dalam database relasional. ORM memungkinkan pengembang untuk berinteraksi dengan database menggunakan objek dan metode Python, tanpa harus menulis query SQL secara langsung. Berikut adalah alasan mengapa model Django disebut ORM:
1) Pemetaan Objek ke Tabel Database:
   - Setiap model di Django adalah representasi dari sebuah tabel di database. Setiap atribut model (seperti name, price, description) dipetakan ke kolom tabel database. Misalnya, model Python yang berisi atribut name akan diterjemahkan menjadi kolom name di tabel database.
2) Manipulasi Data Menggunakan Objek Python:
   - ORM memungkinkan pengembang untuk mengambil, menyimpan, memperbarui, dan menghapus data di database hanya dengan menggunakan objek Python. Misalnya, alih-alih menulis query SQL, pengembang bisa menggunakan metode seperti .save(), .filter(), atau .delete() pada objek model untuk memanipulasi data.
3) Abstraksi Database:
   - Django ORM menyediakan lapisan abstraksi antara kode Python dan database, sehingga pengembang tidak perlu khawatir tentang implementasi spesifik dari database yang digunakan (seperti MySQL, PostgreSQL, atau SQLite). Django akan secara otomatis menghasilkan query SQL yang sesuai berdasarkan model Python.
4) Mengelola Relasi Database:
   - Django ORM juga memungkinkan pengelolaan relasi antar tabel seperti One-to-Many, Many-to-Many, dan One-to-One. Misalnya, relasi antara produk dan kategori dalam sebuah toko online bisa diatur menggunakan ForeignKey atau ManyToManyField.

Contoh sederhana model dalam Django:
from django.db import models

class Product(models.Model):
   name = models.CharField(max_length=100)
   price = models.DecimalField(max_digits=10, decimal_places=2)
   description = models.TextField()

#  Tugas Individu 3 #
#### Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform? ####
- Interaksi pengguna dan sistem: Dalam website atau mobile app, ada interaksi antara user dan sistem melalui timbal balik pengiriman data. Data delivery memastikan input dikirim ke server, diproses, dan dikembalikan ke user. Oleh karena itu, tanpa data delivery yang efektif, interaksi antara user dan server dapat terganggu.
- Integrasi sistem: Komponen Platform Services biasanya saling terhubung. Contohnya yaitu antara front-end dan back-end, dimana front-end yang mengirim request ke back-end dan back-end yang memproses dan mengirim response. Data delivery memastikan bahwa data bisa pindah dengan aman dan efisien antar sistem dan terjadi integrasi yang mulus.
- Peningkatan efisiensi dan kecepatan: Data delivery yang efektif membuat platform bisa bekerja lebih cepat dan efisien. Apabila data dikirim dan diterima dengan cepat, user akan mendapatkan pengalaman yang responsif.
- Peningkatan pengalaman user: Semakin cepat dan akurat data dikirim dan diterima, maka user juga akan mendapatkan pengalaman yang bagus.

#### Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML? ####

JSON lebih baik (dan lebih populer) karena beberapa alasan:
- Better Readability, karena JSON memiliki format yang jauh lebih simpel dibanding XML yang menggunakan opening dan closing tag.
- Ukuran file JSON biasanya lebih kecil karena tidak perlu banyak markup seperti XML. Hal ini membuat pengiriman data melalui jaringan menjadi lebih cepat dan efisien.
- JSON lebih mudah di parse oleh JavaScript tanpa memerlukan library atau tools tambahan. Sedangkan parsing XML lebih rumit karena harus memeriksa opening dan closing tag serta struktur yang rumit.

#### Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut? ####

is_valid() adalah method yang digunakan untuk memeriksa apakah data yang dikirim melalui form sesuai dengan aturan atau validasi yang telah ditentukan. Beberapa yang divalidasi, antara lain: 
- Mengecek apakah semua field sudah diisi
- Mengecek apakah tipe data input sesuai yang diharapkan
- Mengecek apakah data yang di input memenuhi kriteria validasi khusus

Mengapa kita membutuhkan is_valid()? Beberapa alasannya adalah sebagai berikut:
- Mencegah data tidak valid masuk ke database
- Menyediakan pesan error yang berbeda tergantung dari kesalahannya.
- Memastikan data bersih sebelum diproses.
- Dapat melakukan validasi custom.

#### Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang? ####

Dalam Django, csrf_token adalah bagian dari mekanisme CSRF (Cross-Site Request Forgery) protection, yang sangat penting untuk mencegah serangan jenis CSRF pada aplikasi web. CSRF (Cross-Site Request Forgery) adalah serangan di mana penyerang memanfaatkan kepercayaan antara pengguna dan server. Penyerang membuat permintaan ke server tanpa sepengetahuan pengguna, menggunakan kredensial pengguna yang sudah login, seperti cookie. Akibatnya, tindakan seperti mengubah data atau melakukan transaksi bisa terjadi tanpa persetujuan pengguna yang sah.

csrf_token adalah token rahasia yang unik untuk setiap sesi pengguna. Django menambahkan token ini secara otomatis di semua form HTML yang melakukan POST request. Fungsi dari csrf_token adalah untuk memastikan bahwa permintaan yang dikirimkan dari form benar-benar berasal dari pengguna yang sah dan bukan dari situs pihak ketiga yang mencoba melakukan serangan CSRF.

Berikut cara serangan CSRF dapat dieksekusi jika csrf_token tidak diterapkan:
- Penyerang membuat form palsu di situs lain
- Pengguna secara tidak sadar mengirimkan form
- Karena tidak ada proteksi csrf_token, server memproses permintaan tersebut dan menyebabkan kerugian tanpa disadari pengguna.

#### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial). ####

1) Membuat base.html sebagai kerangka / template
2) Membuat input form
   - Membuat forms.py dengan model ProductEntry yang menerima beberapa input: name, price, description
   - Pada views.py, menambahkan create_product_entry yang mengarahkan user dari main page ke input page untuk mengisi produk, sekaligus validasi, memproses, dan menyimpan input. Apabila sudah, akan kembali ke main page.
   - Membuat create_product_entry.html sebagai input page yang menampilkan input form
   - Routing URL form input dengan menambahkan path URL tersebut ke urlpatterns di dalam urls.py
3) Tambah 4 fungsi views baru untuk melihat entry dalam format yang berbeda, yaitu show_xml, show_json, show_xml_by_id, show_json_by_id
4) Membuat routing URL dan masukkan ke urlpatterns dalam urls.py

![show_xml](https://github.com/shaneemichael/fresh-bite/blob/main/components/show_xml.png)
![show_json](https://github.com/shaneemichael/fresh-bite/blob/main/components/show_json.png)
![show_xml_by_id](https://github.com/shaneemichael/fresh-bite/blob/main/components/show_xml_by_id.png)
![show_json_by_id](https://github.com/shaneemichael/fresh-bite/blob/main/components/show_json_by_id.png)