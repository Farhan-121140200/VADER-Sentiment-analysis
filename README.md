#  Analisis Sentimen Komentar Menggunakan Metode VADER

Program ini adalah aplikasi berbasis GUI (antarmuka grafis) yang **menganalisis sentimen dari komentar dalam file CSV**.  
Sentimen yang dianalisis bisa berupa **positif, negatif, atau netral**.

---

## 🔹 Cara Kerja Program
1. **Pengguna memilih file CSV** berisi komentar (dengan nama file bebas).
2. **Program membaca isi file CSV**, menghapus data kosong, dan menerjemahkan komentar jika diperlukan.
3. **Analisis sentimen dilakukan** menggunakan metode **VADER** untuk menentukan apakah komentar **positif, negatif, atau netral**.
4. **Hasil analisis disimpan sebagai file CSV** di lokasi yang sama dengan `main.exe`.
5. Jika file hasil sebelumnya sudah ada, **program akan membuat file baru tanpa menimpa file lama**.

---


## 🔹 Struktur Kode Sederhana
1. **Memuat pustaka yang diperlukan** (`pandas`, `customtkinter`, dll.).
2. **Membuat antarmuka GUI** dengan tombol & label.
3. **Membaca file CSV yang dipilih pengguna**.
4. **Melakukan analisis sentimen dengan VADER**.
5. **Menyimpan hasil di lokasi yang sama dengan `main.exe`**.
6. **Menampilkan hasil di aplikasi** dan memberitahu pengguna jika proses selesai.

---


