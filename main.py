import os
import pandas as pd
import customtkinter as ctk
from tkinter import filedialog, messagebox
from terjemahan import terjemahkan_teks
from sentimen_vader import analisis_sentimen

# Konfigurasi tampilan
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class SentimentApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Analisis Sentimen")
        self.geometry("500x400")
        self.resizable(False, False)

        # Label Instruksi
        self.label_instruksi = ctk.CTkLabel(self, text="🎯 Pilih File CSV:", font=("Arial", 14))
        self.label_instruksi.pack(pady=10)

        # Tombol Pilih File
        self.btn_browse = ctk.CTkButton(self, text="Pilih File", command=self.browse_file)
        self.btn_browse.pack(pady=5)

        # Label Status
        self.label_status = ctk.CTkLabel(self, text="🚀 Belum ada file dipilih!", font=("Arial", 12), text_color="gray")
        self.label_status.pack()

        # Tombol Proses Sentimen
        self.btn_proses = ctk.CTkButton(self, text="Proses Sentimen", command=self.process_sentiment, fg_color="green", hover_color="darkgreen")
        self.btn_proses.pack(pady=10)

        # Progress Bar
        self.progress = ctk.CTkProgressBar(self, width=300)
        self.progress.pack(pady=5)
        self.progress.set(0)  # Mulai dari 0

        # Label Hasil Sentimen
        self.label_hasil = ctk.CTkLabel(self, text="", font=("Arial", 12), text_color="white")
        self.label_hasil.pack(pady=10)

        # Variabel file path
        self.csv_path = ""

    def browse_file(self):
        """ Pilih file CSV secara manual """
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if file_path:
            self.csv_path = file_path
            self.label_status.configure(text=f"📂 File: {os.path.basename(file_path)}", text_color="green")

    def process_sentiment(self):
        """ Proses analisis sentimen dari file CSV """
        if not self.csv_path:
            messagebox.showerror("Error", "Silakan pilih file CSV terlebih dahulu!")
            return

        try:
            self.progress.set(0.2)  # Update progress bar

            # Coba membaca CSV dengan header
            try:
                df = pd.read_csv(self.csv_path, usecols=["comment"])
            except:
                df = pd.read_csv(self.csv_path, usecols=[1], names=["comment"], skiprows=1)  # Jika tidak ada header

            self.progress.set(0.4)

            # Pastikan tidak ada NaN di kolom komentar
            df["comment"] = df["comment"].fillna("")

            # Terjemahkan teks dan pastikan hasilnya tidak None
            df["translated"] = df["comment"].apply(lambda teks: terjemahkan_teks(teks) if teks.strip() else "")
            df["translated"] = df["translated"].fillna("")  # Pastikan tidak ada nilai None

            self.progress.set(0.6)

            # Lakukan analisis sentimen
            df["sentimen"] = df["translated"].apply(lambda teks: analisis_sentimen(teks)["sentimen"] if teks.strip() else "netral")

            self.progress.set(0.8)

            # Hitung jumlah sentimen
            jumlah_positif = (df["sentimen"] == "positif").sum()
            jumlah_negatif = (df["sentimen"] == "negatif").sum()
            jumlah_netral = (df["sentimen"] == "netral").sum()

            # Cari nama file yang belum digunakan
            output_folder = os.path.dirname(self.csv_path)
            output_base = "hasil_sentimen"
            output_file = os.path.join(output_folder, f"{output_base}.csv")

            counter = 1
            while os.path.exists(output_file):  # Jika file sudah ada, tambahkan nomor
                output_file = os.path.join(output_folder, f"{output_base}_{counter}.csv")
                counter += 1

            # Simpan hasil ke file CSV
            df[["comment", "sentimen"]].to_csv(output_file, index=False)

            self.progress.set(1)  # Proses selesai

            # Tampilkan hasil di label
            hasil_text = f"✅ Analisis selesai!\n📊 Positif: {jumlah_positif} | Negatif: {jumlah_negatif} | Netral: {jumlah_netral}\n💾 Hasil: {os.path.basename(output_file)}"
            self.label_hasil.configure(text=hasil_text, text_color="lightblue")

            messagebox.showinfo("Sukses", f"✅ Analisis selesai! Hasil tersimpan di:\n{output_file}")

        except Exception as e:
            self.progress.set(0)  # Reset progress jika gagal
            messagebox.showerror("Error", f"Gagal memproses file:\n{str(e)}")

# Jalankan aplikasi
if __name__ == "__main__":
    app = SentimentApp()
    app.mainloop()
