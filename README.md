# 📌 Analisis Sentimen Komentar (CSV)

## 🔹 Apa yang Dilakukan Program Ini?
Program ini adalah aplikasi berbasis GUI (antarmuka grafis) yang **menganalisis sentimen dari komentar dalam file CSV**.  
Sentimen yang dianalisis bisa berupa **positif, negatif, atau netral**.

---

## 🔹 Bagaimana Cara Kerjanya?
1. **Pengguna memilih file CSV** berisi komentar (dengan nama file bebas).
2. **Program membaca isi file CSV**, menghapus data kosong, dan menerjemahkan komentar jika diperlukan.
3. **Analisis sentimen dilakukan** menggunakan metode **VADER** untuk menentukan apakah komentar **positif, negatif, atau netral**.
4. **Hasil analisis disimpan sebagai file CSV** di lokasi yang sama dengan `main.exe`.
5. Jika file hasil sebelumnya sudah ada, **program akan membuat file baru tanpa menimpa file lama**.

---

## 🔹 Fitur Utama Program
✅ **Mudah digunakan** → Tinggal pilih file CSV, klik "Proses Sentimen", dan hasilnya langsung tersedia.  
✅ **GUI yang sederhana & modern** → Dibuat dengan **CustomTkinter** untuk tampilan yang lebih menarik.  
✅ **Mencegah hasil tertimpa** → Jika `hasil_sentimen.csv` sudah ada, akan dibuat `hasil_sentimen_1.csv`, `hasil_sentimen_2.csv`, dst.  
✅ **Dapat digunakan sebagai aplikasi standalone (`.exe`)** → Hasil tetap tersimpan di folder `main.exe`.  
✅ **Progress bar** → Menampilkan progres saat data sedang diproses.  
✅ **Dapat membaca file CSV dengan format & nama yang fleksibel**.

---

## 🔹 Tampilan Aplikasi
1️⃣ **Tombol untuk memilih file CSV**  
2️⃣ **Tombol untuk memproses sentimen**  
3️⃣ **Indikator progres bar saat proses berjalan**  
4️⃣ **Hasil analisis ditampilkan di layar dan disimpan sebagai file CSV**

---

## 🔹 Struktur Kode Sederhana
1. **Memuat pustaka yang diperlukan** (`pandas`, `customtkinter`, dll.).
2. **Membuat antarmuka GUI** dengan tombol & label.
3. **Membaca file CSV yang dipilih pengguna**.
4. **Melakukan analisis sentimen dengan VADER**.
5. **Menyimpan hasil di lokasi yang sama dengan `main.exe`**.
6. **Menampilkan hasil di aplikasi** dan memberitahu pengguna jika proses selesai.

---

## 🔹 Cara Menggunakan Program
1. **Jalankan program (`main.exe`)**.
2. Klik **"Pilih File"** dan cari file CSV yang berisi komentar.
3. Klik **"Proses Sentimen"** untuk memulai analisis.
4. Setelah selesai, program akan menyimpan hasil di **folder yang sama dengan `main.exe`**.
5. **Buka file `hasil_sentimen.csv`** untuk melihat hasil analisis.

---

### 🎯 **Kesimpulan**
Program ini membantu **menganalisis sentimen komentar dengan mudah** dan **menyimpan hasilnya tanpa tertimpa**.  
Cocok untuk **penelitian, analisis media sosial, atau proyek NLP sederhana**! 🚀😊
