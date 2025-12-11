# 🎓 Sistem Manajemen Mahasiswa

<div align="center">

![Python](https://img.shields.io/badge/Python-3.13-blue.svg)
![Data Structure](https://img.shields.io/badge/Data%20Structure-Red%20Black%20Tree-red.svg)

**Sistem manajemen data mahasiswa berbasis console menggunakan Red-Black Tree**

</div>

---

## 🎯 Tentang Project

<p align="justify">
Sistem Manajemen Mahasiswa adalah aplikasi console-based yang dikembangkan untuk mengelola data mahasiswa secara efisien. Project ini dibuat sebagai bagian dari tugas mata kuliah Struktur Data dengan mengimplementasikan <strong>Red-Black Tree</strong> sebagai struktur data utama.
</p>

### Mengapa Red-Black Tree?

<ul>
<li><strong>Self-Balancing</strong>: Menjamin operasi tetap efisien dengan kompleksitas O(log n)</li>
<li><strong>Performa Optimal</strong>: Cocok untuk operasi search, insert, dan delete yang sering dilakukan</li>
<li><strong>Konsistensi</strong>: Tinggi tree maksimal 2 log(n+1), mencegah worst-case O(n)</li>
</ul>

---

## 🌳 Struktur Data

### Red-Black Tree Properties

<ol>
<li>Setiap node berwarna merah atau hitam</li>
<li>Root selalu berwarna hitam</li>
<li>Setiap leaf (NIL) berwarna hitam</li>
<li>Jika node berwarna merah, maka kedua child-nya hitam</li>
<li>Setiap path dari node ke descendant leaf mengandung jumlah black node yang sama</li>
</ol>

### Operasi Utama

```python
# Insert: O(log n)
tree.insert(nim, nama, jurusan, ipk)

# Search: O(log n)
node = tree.search(nim)

# Delete: O(log n)
tree.delete_node(nim)

# Traversal: O(n)
students = tree.get_all_students()
```

---

## ✨ Fitur

<table>
<tr>
<td>

### 🔹 CRUD Operations
- Tambah data mahasiswa
- Cari mahasiswa (by NIM)
- Update data mahasiswa
- Hapus data mahasiswa

</td>
<td>

### 🔹 Fitur Tambahan
- Statistik lengkap (IPK, jurusan)
- Persistensi data (CSV)
- Tampilan tabel yang rapi
- Performa cepat dengan RBT

</td>
</tr>
</table>

---

## 💻 Persyaratan Sistem

<pre>
• Python 3.8 atau lebih tinggi
• Library: tabulate
• OS: Windows / Linux / MacOS
</pre>

---

## 🚀 Instalasi

### 1. Clone Repository

```bash
git clone https://github.com/username/sistem-manajemen-mahasiswa.git
cd sistem-manajemen-mahasiswa
```

### 2. Install Dependencies

```bash
pip install tabulate
```

### 3. Jalankan Aplikasi

```bash
python main.py
```

---

## 📖 Cara Penggunaan

### Menu Utama

```
==================================================
         SISTEM MANAJEMEN MAHASISWA
==================================================
1. Tambah Mahasiswa
2. Cari Mahasiswa
3. Update Mahasiswa
4. Hapus Mahasiswa
5. Tampilkan Semua Mahasiswa
6. Statistik
0. Keluar
==================================================
```

### Contoh Penggunaan

#### ➕ Tambah Mahasiswa

```
Pilih menu: 1
NIM: 242410103001
Nama: John Doe
Jurusan: Informatika
IPK: 3.75
```

#### 🔍 Cari Mahasiswa

```
Pilih menu: 2
Masukkan NIM: 242410103001

Data Mahasiswa:
NIM     : 242410103001
Nama    : John Doe
Jurusan : Informatika
IPK     : 3.75
```

#### 📊 Statistik

```
Pilih menu: 6

Total Mahasiswa: 13
Rata-rata IPK: 3.59
IPK Tertinggi: 3.95 (Dimas Aditama)
IPK Terendah: 3.01 (Farhan Malik)

Jumlah Mahasiswa per Jurusan:
  • Informatika: 6 mahasiswa (Rata-rata IPK: 3.73)
  • Sistem Informasi: 4 mahasiswa (Rata-rata IPK: 3.56)
  • Teknologi Informasi: 3 mahasiswa (Rata-rata IPK: 3.30)
```

---

## 📁 Struktur File

```
sistem-manajemen-mahasiswa/
│
├── main.py                 # Entry point aplikasi
├── manajemen.py           # Class ManajemenMahasiswa & logika bisnis
├── rbt.py                 # Implementasi Red-Black Tree
├── data_mahasiswa.csv     # Database (auto-generated)
```

### Penjelasan File

<dl>
<dt><strong>main.py</strong></dt>
<dd>File utama untuk menjalankan aplikasi</dd>

<dt><strong>manajemen.py</strong></dt>
<dd>Berisi class ManajemenMahasiswa yang mengelola operasi CRUD dan UI</dd>

<dt><strong>rbt.py</strong></dt>
<dd>Implementasi Red-Black Tree dari nol tanpa library eksternal</dd>

<dt><strong>data_mahasiswa.csv</strong></dt>
<dd>File penyimpanan data mahasiswa dalam format CSV</dd>
</dl>

---

## ⚡ Kompleksitas Algoritma

<table border="1">
<thead>
<tr>
<th>Operasi</th>
<th>Time Complexity</th>
<th>Space Complexity</th>
</tr>
</thead>
<tbody>
<tr>
<td>Insert</td>
<td>O(log n)</td>
<td>O(1)</td>
</tr>
<tr>
<td>Search</td>
<td>O(log n)</td>
<td>O(log n) - rekursif</td>
</tr>
<tr>
<td>Delete</td>
<td>O(log n)</td>
<td>O(1)</td>
</tr>
<tr>
<td>Traversal</td>
<td>O(n)</td>
<td>O(n)</td>
</tr>
<tr>
<td>Rotate</td>
<td>O(1)</td>
<td>O(1)</td>
</tr>
</tbody>
</table>

### Penjelasan Kompleksitas

<blockquote>
<p><strong>Mengapa O(log n)?</strong></p>
<p>Red-Black Tree memastikan tree tetap seimbang dengan tinggi maksimal 2 log(n+1). Setiap operasi insert, search, dan delete hanya perlu melewati tinggi tree, sehingga kompleksitasnya O(log n).</p>
</blockquote>

---

<div align="center">

### ⭐ Jika project ini bermanfaat, berikan star!

**Made with ❤️ by Tim Struktur Data**

</div>
