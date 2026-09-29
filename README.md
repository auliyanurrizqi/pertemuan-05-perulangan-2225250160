# Pertemuan 05 Perulangan Python

**Nama:** Aulia Nurrizqi
**NIM:** 225250160
**Kelas:** 3A

## Tujuan

Pada Pertemuan 05, saya mempelajari konsep perulangan dalam Python menggunakan `for` dan `while`.

Tujuan pembelajaran:

* Memahami konsep iterasi, kondisi berhenti, dan perubahan nilai variabel.
* Menggunakan `for` dengan `range`.
* Menggunakan `while` dengan kondisi tertentu.
* Menentukan nilai awal, kondisi, dan pembaruan variabel kontrol.
* Menggabungkan seleksi `if` dengan perulangan.
* Menggunakan akumulasi dan pencacahan.
* Melakukan tracing dan debugging perulangan di VS Code.
* Menguji program menggunakan beberapa test case.
* Mengelola commit dan push hasil pekerjaan melalui GitHub.

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
```

## Materi yang Dipelajari

### 1. Perulangan `for`

Perulangan `for` digunakan ketika jumlah iterasi telah diketahui atau program akan mengunjungi suatu urutan nilai yang jelas.

Contoh:

```python
for i in range(1, 6):
    print(i)
```

### 2. Fungsi `range()`

`range()` digunakan untuk menghasilkan urutan bilangan.

Contoh:

```python
range(5)
```

menghasilkan:

```text
0, 1, 2, 3, 4
```

Nilai batas akhir tidak termasuk dalam hasil.

### 3. Perulangan `while`

Perulangan `while` digunakan ketika proses berjalan selama suatu kondisi bernilai `True`.

Contoh:

```python
i = 1

while i <= 5:
    print(i)
    i = i + 1
```

Pada `while`, terdapat tiga komponen penting:

* Nilai awal
* Kondisi
* Pembaruan variabel

Pembaruan variabel diperlukan agar kondisi pada akhirnya menjadi `False` dan program berhenti.

### 4. Seleksi di dalam Perulangan

Seleksi `if` dapat digunakan di dalam perulangan untuk menentukan apakah suatu nilai memenuhi kondisi tertentu.

Contoh:

```python
for bilangan in range(1, 11):
    if bilangan % 2 == 0:
        print(bilangan)
```

### 5. Akumulasi

Akumulasi digunakan untuk menggabungkan nilai secara berulang.

Contoh:

```python
total = 0

for i in range(1, 6):
    total = total + i

print(total)
```

Hasilnya adalah:

```text
15
```

## Latihan

### Latihan 1 — Tabel Perkalian

File:

```text
latihan/01_tabel_perkalian.py
```

Program menerima satu bilangan bulat dan menampilkan perkalian bilangan tersebut dari 1 sampai 10.

**Test case:**

* `n = 4`
* `n = -3`

Jumlah baris keluaran harus tetap 10.

### Latihan 2 — Jumlah Bilangan

File:

```text
latihan/02_jumlah_bilangan.py
```

Program menghitung jumlah:

```text
1 + 2 + ... + n
```

**Test case:**

* `n = 1` menghasilkan `1`
* `n = 5` menghasilkan `15`
* `n = 10` menghasilkan `55`

### Latihan 3 — Validasi Input

File:

```text
latihan/03_validasi_input.py
```

Program meminta nilai ujian dari 0 sampai 100. Jika input berada di luar rentang tersebut, program akan meminta input kembali.

**Test case:**

```text
120 → ditolak
-5  → ditolak
75  → diterima
```

### Latihan 4 — Menghitung Bilangan Genap

File:

```text
latihan/04_hitung_genap.py
```

Program menghitung banyak bilangan genap dari 1 sampai `n`.

**Hasil yang diharapkan:**

| n  | Banyak Bilangan Genap |
| -- | --------------------: |
| 1  |                     0 |
| 2  |                     1 |
| 5  |                     2 |
| 10 |                     5 |

## Kuis 2 — Deret Aritmetika

File:

```text
kuis/kuis2_deret_aritmetika.py
```

Program menerima:

* Suku pertama `a`
* Beda `d`
* Banyak suku `n`

Program menggunakan `while` untuk melakukan validasi `n` dan menggunakan `for` untuk menghasilkan deret.

### Algoritma

1. Membaca suku pertama `a`.
2. Membaca beda `d`.
3. Membaca banyak suku `n`.
4. Jika `n <= 0`, meminta input `n` kembali sampai valid.
5. Menetapkan `total = 0`.
6. Melakukan perulangan sebanyak `n` kali.
7. Menghitung suku dengan:

```text
suku = a + i × d
```

8. Menambahkan setiap suku ke `total`.
9. Menampilkan setiap suku.
10. Menampilkan jumlah seluruh suku.

### Test Case Kuis 2

|   a |   d |  n | Suku            | Jumlah |
| --: | --: | -: | --------------- | -----: |
|   2 |   3 |  5 | 2, 5, 8, 11, 14 |     40 |
|  10 |  -2 |  4 | 10, 8, 6, 4     |     28 |
| 1.5 | 0.5 |  3 | 1.5, 2.0, 2.5   |    6.0 |

## Cara Menjalankan Program

Pastikan Python sudah terpasang dan folder proyek sudah dibuka melalui VS Code.

Untuk menjalankan latihan:

```bash
python latihan/01_tabel_perkalian.py
```

Contoh menjalankan kuis:

```bash
python kuis/kuis2_deret_aritmetika.py
```

Jika menggunakan `python3`:

```bash
python3 kuis/kuis2_deret_aritmetika.py
```

## Kuis Formatif

### 1. Apa keluaran `list(range(1, 6))`?

**Jawaban:** `[1, 2, 3, 4, 5]`

### 2. Mengapa `range(1, 10)` tidak menghasilkan 10?

**Jawaban:** Karena nilai `stop` pada `range()` tidak termasuk dalam hasil. `range(1, 10)` menghasilkan angka 1 sampai 9.

### 3. Kapan `for` lebih sesuai daripada `while`?

**Jawaban:** `for` lebih sesuai ketika jumlah iterasi sudah diketahui atau terdapat urutan nilai yang jelas.

### 4. Sebutkan tiga komponen utama yang harus diperiksa pada `while`.

**Jawaban:**

1. Nilai awal.
2. Kondisi.
3. Pembaruan variabel.

### 5. Apa penyebab paling umum infinite loop?

**Jawaban:** Variabel kontrol tidak diperbarui sehingga kondisi `while` tidak pernah menjadi `False`.

### 6. Apa nilai akhir `total` setelah menjumlahkan 1 sampai 5 dengan loop?

**Jawaban:** `15`

Perhitungannya:

```text
1 + 2 + 3 + 4 + 5 = 15
```

### 7. Mengapa `total = 0` biasanya ditulis sebelum loop?

**Jawaban:** Karena `total` harus memiliki nilai awal sebelum proses penjumlahan berulang dilakukan. Jika diletakkan di dalam loop, nilai total akan terus di-reset.

### 8. Bagaimana seleksi `if` dapat digunakan di dalam loop?

**Jawaban:** Seleksi `if` digunakan untuk menentukan apakah setiap nilai yang sedang diproses memenuhi kondisi tertentu, misalnya untuk menghitung bilangan genap.

### 9. Apa fungsi `git commit`?

**Jawaban:** `git commit` berfungsi untuk merekam perubahan yang telah dilakukan ke dalam riwayat Git secara lokal.

### 10. Perintah apa yang mengirim commit terbaru ke GitHub setelah remote tersambung?

**Jawaban:**

```bash
git push
```

## Refleksi

Pada Pertemuan 05, saya memahami bahwa `for` digunakan ketika jumlah perulangan atau urutan nilai sudah diketahui, sedangkan `while` digunakan ketika perulangan bergantung pada suatu kondisi.

Saya juga memahami pentingnya nilai awal, kondisi berhenti, dan pembaruan variabel pada `while`. Jika variabel kontrol tidak diperbarui dengan benar, program dapat mengalami infinite loop.

Selain itu, saya memahami penggunaan `if` di dalam perulangan untuk melakukan seleksi terhadap setiap nilai yang diproses serta penggunaan akumulator untuk menghitung jumlah secara berulang.

## Kesimpulan

Perulangan `for` dan `while` merupakan struktur penting dalam pemrograman Python untuk menjalankan proses secara berulang. Penggunaan perulangan harus memperhatikan nilai awal, kondisi, batas iterasi, dan pembaruan variabel agar program dapat berhenti dengan benar.

Melalui latihan dan Kuis 2, saya dapat menerapkan perulangan untuk membuat tabel perkalian, menghitung jumlah bilangan, melakukan validasi input, menghitung bilangan genap, serta menghitung deret aritmetika.

## Sumber

* Bahan Ajar Algoritma dan Pemrograman Pertemuan 05, Program Studi S1 Pendidikan Matematika FKIP Untirta.
* Python Software Foundation. Python 3 Documentation: Control Flow Tools.
* Visual Studio Code Documentation: Python in Visual Studio Code.
* GitHub Docs: Creating a New Repository dan Adding Locally Hosted Code to GitHub.
