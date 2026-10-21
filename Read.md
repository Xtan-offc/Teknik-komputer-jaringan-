XTAN TKJ TOOLKIT

Network & Linux Learning Tools — Powered by Xtan

XTAN TKJ TOOLKIT adalah tools berbasis Python yang dirancang untuk membantu pelajar TKJ (Teknik Komputer dan Jaringan) mempelajari dasar-dasar jaringan komputer, administrasi Linux, troubleshooting koneksi, dan informasi sistem melalui terminal Termux.

Tools ini menggunakan antarmuka terminal berwarna dengan menu interaktif yang sederhana, sehingga mudah digunakan oleh pemula maupun pelajar yang sedang berlatih administrasi jaringan.

Fitur Utama

- Network Information — Menampilkan informasi IP, interface jaringan, routing, dan DNS resolver.
- Ping Test — Menguji konektivitas jaringan dan waktu respons host.
- DNS Lookup — Memeriksa informasi resolusi domain.
- IPv4 Subnet Calculator — Menghitung network address, subnet mask, broadcast address, prefix, dan jumlah alamat IP.
- HTTP Header Checker — Memeriksa status HTTP dan header respons dari URL yang diizinkan.
- Traceroute — Membantu mempelajari jalur jaringan menuju host tujuan.
- System Information — Menampilkan informasi sistem operasi, arsitektur, Python, dan hostname.
- Linux Command Guide — Panduan perintah dasar Linux dan jaringan.
- Report Logger — Menyimpan hasil pemeriksaan ke file "laporan_tkj.txt".
- Interactive Terminal UI — Menu navigasi angka dengan teks berwarna.
- Error Handling — Menangani input yang tidak valid, perintah yang tidak tersedia, dan kegagalan koneksi.

Teknologi

- Python 3
- Termux
- Linux command-line utilities
- Python standard library

Persyaratan

- Perangkat Android dengan Termux.
- Koneksi internet untuk pemeriksaan jaringan eksternal dan instalasi paket.
- Python 3 dan paket sistem yang dibutuhkan.

Instalasi

Perbarui paket Termux:

pkg update && pkg upgrade -y

Instal dependensi:

pkg install python iproute2 iputils dnsutils curl traceroute -y

Buat direktori project:

mkdir -p ~/xtan-tkj
cd ~/xtan-tkj

Simpan kode utama sebagai:

xtan_tkj.py

Menjalankan Tools

Jalankan perintah:

python xtan_tkj.py

Pilih menu yang tersedia dengan memasukkan nomor fitur pada terminal.

Struktur Project

xtan-tkj/
├── xtan_tkj.py
├── README.md
└── laporan_tkj.txt

File "laporan_tkj.txt" akan dibuat secara otomatis setelah laporan berhasil disimpan.

Contoh Penggunaan

Menghitung subnet IPv4

Masukkan alamat:

192.168.1.10/24

Tools akan menampilkan alamat IP, prefix, subnet mask, network address, broadcast address, dan jumlah alamat IP yang tersedia.

Menguji koneksi

Pilih menu Ping Test, lalu masukkan host yang ingin diperiksa, misalnya:

example.com

Memeriksa DNS

Pilih DNS Lookup dan masukkan nama domain untuk melihat hasil resolusinya.

Tujuan Pembelajaran

XTAN TKJ TOOLKIT dapat digunakan untuk latihan:

- Dasar-dasar TCP/IP dan IPv4.
- Subnetting dan pengalamatan jaringan.
- DNS dan resolusi nama domain.
- Troubleshooting konektivitas.
- Dasar administrasi Linux.
- Pemahaman HTTP response headers.
- Pengumpulan laporan praktikum jaringan.

Keamanan dan Batasan

Tools ini ditujukan untuk pembelajaran dan troubleshooting jaringan yang sah. Lakukan pemeriksaan hanya pada perangkat, domain, dan jaringan yang kamu miliki atau telah mendapat izin untuk mengujinya.

Hasil pemeriksaan dapat berbeda bergantung pada versi Android, konfigurasi Termux, ketersediaan paket, kebijakan jaringan, dan dukungan server tujuan. Tidak semua fitur dijamin berfungsi pada setiap perangkat tanpa penyesuaian.

Pengembang

XTAN TKJ TOOLKIT

Developer: Xtan
Community: Xyro Community
Platform: Termux / Android
Language: Python 3
Version: 1.0.0

Powered by Xtan

Belajar jaringan. Pahami Linux. Bangun kemampuan TKJ.
