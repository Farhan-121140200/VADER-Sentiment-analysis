# VADER-Sentiment-analysiss
Sentiment Analysis Using VADER

📌 Penjelasan Sederhana Program Analisis Sentimen
🔹 Apa yang Dilakukan Program Ini?
Program ini adalah aplikasi berbasis GUI (antarmuka grafis) yang menganalisis sentimen dari komentar dalam file CSV.
Sentimen yang dianalisis bisa berupa positif, negatif, atau netral.

🔹 Bagaimana Cara Kerjanya?
Pengguna memilih file CSV berisi komentar (dengan nama file bebas).
Program membaca isi file CSV, menghapus data kosong, dan menerjemahkan komentar jika diperlukan.
Analisis sentimen dilakukan menggunakan metode VADER untuk menentukan apakah komentar positif, negatif, atau netral.
Hasil analisis disimpan sebagai file CSV di lokasi yang sama dengan main.exe.
Jika file hasil sebelumnya sudah ada, program akan membuat file baru tanpa menimpa file lama.
🔹 Fitur Utama Program
✅ Mudah digunakan → Tinggal pilih file CSV, klik "Proses Sentimen", dan hasilnya langsung tersedia.
✅ GUI yang sederhana & modern → Dibuat dengan CustomTkinter untuk tampilan yang lebih menarik.
✅ Mencegah hasil tertimpa → Jika hasil_sentimen.csv sudah ada, akan dibuat hasil_sentimen_1.csv, hasil_sentimen_2.csv, dst.
✅ Dapat digunakan sebagai aplikasi standalone (.exe) → Hasil tetap tersimpan di folder main.exe.
✅ Progress bar → Menampilkan progres saat data sedang diproses.
✅ Dapat membaca file CSV dengan format & nama yang fleksibel.

🔹 Tampilan Aplikasi
1️⃣ Tombol untuk memilih file CSV
2️⃣ Tombol untuk memproses sentimen
3️⃣ Indikator progres bar saat proses berjalan
4️⃣ Hasil analisis ditampilkan di layar dan disimpan sebagai file CSV

🔹 Struktur Kode Sederhana
Memuat pustaka yang diperlukan (pandas, customtkinter, dll.).
Membuat antarmuka GUI dengan tombol & label.
Membaca file CSV yang dipilih pengguna.
Melakukan analisis sentimen dengan VADER.
Menyimpan hasil di lokasi yang sama dengan main.exe.
Menampilkan hasil di aplikasi dan memberitahu pengguna jika proses selesai.
🔹 Bagaimana Cara Menggunakannya?
Jalankan program (main.exe).
Klik "Pilih File" dan cari file CSV yang berisi komentar.
Klik "Proses Sentimen" untuk memulai analisis.
Setelah selesai, program akan menyimpan hasil di folder yang sama dengan main.exe.
Buka file hasil_sentimen.csv untuk melihat hasil analisis.
🎯 Kesimpulan
Program ini membantu menganalisis sentimen komentar dengan mudah dan menyimpan hasilnya tanpa tertimpa.
Cocok untuk penelitian, analisis media sosial, atau proyek NLP sederhana! 🚀😊
