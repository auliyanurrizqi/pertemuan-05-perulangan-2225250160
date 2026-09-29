# Pertemuan 05 Perulangan Python

**Nama:** Aulia Nurrizqi  
**NIM:** 2225250160
**Kelas:** 3A

## Tujuan

Pada Pertemuan 05, saya mempelajari konsep perulangan dalam Python menggunakan `for` dan `while`.

Tujuan pembelajaran:
- Memahami konsep iterasi dan kondisi berhenti.
- Menggunakan `for` dengan `range`.
- Menggunakan `while` dengan kondisi tertentu.
- Menggabungkan perulangan dengan seleksi `if`.
- Menggunakan akumulasi dan pencacahan.
- Melakukan tracing dan debugging program di VS Code.
- Menguji program menggunakan beberapa test case.
- Mengunggah hasil pekerjaan ke GitHub.

## Struktur Folder

```text
pertemuan-05-perulangan-NIM/
│
├── README.md
├── .gitignore
│
├── latihan/
│   ├── 01_tabel_perkalian.py
│   ├── 02_jumlah_bilangan.py
│   ├── 03_validasi_input.py
│   └── 04_hitung_genap.py
│
└── kuis/
    └── kuis2_deret_aritmetika.py
Cara Menjalankan

Pastikan Python sudah terpasang pada komputer dan folder proyek sudah dibuka melalui VS Code.

Contoh menjalankan program:

python latihan/01_tabel_perkalian.py

Untuk menjalankan kuis:

python kuis/kuis2_deret_aritmetika.py

Pada beberapa sistem operasi, perintah Python dapat menggunakan:

python3
Algoritma Kuis 2

Program Kuis 2 digunakan untuk menampilkan deret aritmetika dan menghitung jumlah seluruh suku.

Langkah-langkah algoritma:

Memasukkan suku pertama a.
Memasukkan beda d.
Memasukkan banyak suku n.
Memvalidasi n menggunakan while.
Jika n <= 0, program meminta input n kembali.
Menginisialisasi total = 0.
Menggunakan for untuk melakukan perulangan sebanyak n kali.
Menghitung setiap suku dengan rumus:
suku = a + i * d
Menambahkan setiap suku ke dalam total.
Menampilkan setiap suku dan jumlah akhir deret.
Hasil Pengujian
Test Case 1
Input	Hasil yang Diharapkan	Hasil Aktual	Status
a = 2, d = 3, n = 5	2, 5, 8, 11, 14; Jumlah = 40	2, 5, 8, 11, 14; Jumlah = 40	Berhasil
Test Case 2
Input	Hasil yang Diharapkan	Hasil Aktual	Status
a = 10, d = -2, n = 4	10, 8, 6, 4; Jumlah = 28	10, 8, 6, 4; Jumlah = 28	Berhasil
Test Case 3
Input	Hasil yang Diharapkan	Hasil Aktual	Status
a = 1.5, d = 0.5, n = 3	1.5, 2.0, 2.5; Jumlah = 6.0	1.5, 2.0, 2.5; Jumlah = 6.0	Berhasil
Refleksi

Pada pertemuan ini saya memahami bahwa for digunakan ketika jumlah perulangan atau urutan nilai sudah diketahui, sedangkan while digunakan ketika perulangan bergantung pada suatu kondisi.

Kesalahan yang perlu diperhatikan dalam perulangan adalah batas range, kondisi berhenti, dan pembaruan variabel. Jika variabel kontrol pada while tidak diperbarui, dapat terjadi infinite loop.

Saya juga memahami bahwa variabel akumulator seperti total harus diinisialisasi sebelum perulangan agar nilainya tidak terus di-reset pada setiap iterasi.

Kesimpulan

Perulangan for dan while dapat digunakan untuk menyelesaikan masalah yang membutuhkan proses berulang. Penggunaan perulangan harus memperhatikan nilai awal, kondisi, batas iterasi, serta perubahan variabel agar program dapat berhenti dengan benar dan menghasilkan output yang sesuai.