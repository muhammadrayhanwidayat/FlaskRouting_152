from flask import Flask, redirect, url_for, request, render_template
# Mengimpor Flask dan modul terkait:
# - Flask: Framework untuk membuat aplikasi web.
# - redirect: Mengarahkan pengguna ke URL lain.
# - url_for: Membuat URL berdasarkan nama fungsi endpoint.
# - request: Mengakses data yang dikirim melalui HTTP (GET/POST).
# - render_template: Merender file HTML sebagai tampilan.
app = Flask(__name__)  # Membuat instance aplikasi Flask.
@app.route("/")  # Menentukan route untuk halaman utama.
def index():
   return render_template("login.html")  # Merender file HTML bernama 'login.html'.

@app.route("/about")  # Menentukan route untuk halaman utama.
def about():
   return render_template("about.html")  # Merender file HTML bernama 'login.html'.

@app.route('/success/<name>')  # Route untuk halaman sukses dengan parameter 'name'.
def success(name):
   return 'welcome %s' % name  # Mengembalikan pesan selamat datang dengan nama.

@app.route('/login', methods=['POST', 'GET'])  # Route untuk login, menerima metode GET dan POST.
def login():
   if request.method == 'POST':  # Jika metode HTTP adalah POST:
      user = request.form['nm']  # Ambil nilai dari input form dengan nama 'nm'.
      return redirect(url_for('success', name=user))  # Arahkan ke halaman sukses dengan nama pengguna.
   else:  # Jika metode HTTP adalah GET:
      user = request.args.get('nm')  # Ambil nilai dari query string dengan kunci 'nm'.
      return redirect(url_for('success', name=user))  # Arahkan ke halaman sukses dengan nama pengguna.

if __name__ == '__main__':  # Mengeksekusi aplikasi jika dijalankan langsung.
   app.run(debug=True)  # Menjalankan aplikasi Flask dalam mode debug.


#catatan project
"""
Aplikasi Flask sederhana untuk demonstrasi form login dan pengalihan.

Fungsi Utama:
1. Halaman utama (`/`) menampilkan form login menggunakan template HTML.
2. Halaman `/login` menerima input pengguna melalui metode GET atau POST.
3. Halaman `/success/<name>` menyapa pengguna berdasarkan input yang diterima.
1. Halaman about (`/about`) menampilkan tentang projek ini.

Penjelasan Komponen:
- Import Flask dan modul terkait:
  - Flask: Framework mikro untuk pengembangan aplikasi web.
  - redirect: Mengarahkan pengguna ke URL lain.
  - url_for: Membuat URL berdasarkan nama fungsi endpoint Flask.
  - request: Mengakses data HTTP yang dikirim (GET atau POST).
  - render_template: Merender template HTML dengan Jinja2.

- Route dan Fungsinya:
  1. `/`:
     - Fungsi `index` merender file `login.html` yang berisi form login.
     - File `login.html` harus ada di direktori `templates`.

  2. `/success/<name>`:
     - Fungsi `success` menyapa pengguna dengan pesan berbasis nama yang diberikan.
     - Nama diteruskan sebagai parameter URL.

  3. `/login`:
     - Fungsi `login` menangani data dari form login.
     - Jika metode POST:
       - Data diambil dari form menggunakan `request.form['nm']`.
       - Pengguna diarahkan ke `/success/<name>` dengan nama yang diberikan.
     - Jika metode GET:
       - Data diambil dari query string menggunakan `request.args.get('nm')`.
       - Pengguna diarahkan ke `/success/<name>`.
  1. `/about`:
     - Fungsi `about` merender file `about.html` yang berisi penjelasan project.
     - File `about.html` harus ada di direktori `templates`.



  - `app.run(debug=True)` menjalankan server dalam mode debug.


Cara Kerja:
1. Pengguna membuka halaman utama (`/`) dan melihat form login.
2. Pengguna mengisi nama dan mengirimkan form.
3. Fungsi `login` memproses input:
   - Jika POST, data dari form diproses.
   - Jika GET, data dari URL query string diproses.
4. Pengguna diarahkan ke `/success/<name>` untuk melihat pesan selamat datang.

Catatan:
- Template `login.html` harus dibuat dan diletakkan di folder `templates`.
- Pastikan Flask terinstal dan dijalankan di lingkungan Python yang mendukung.
"""
