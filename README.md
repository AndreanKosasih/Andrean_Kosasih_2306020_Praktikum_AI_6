# Andrean_Kosasih_2306020_Praktikum_AI_6

# 🧠 Sistem Pakar: Certainty Factor & Fuzzy Logic

📌 **Deskripsi**  
Repository ini berisi implementasi sistem pakar berbasis dua pendekatan logika populer, yaitu **Certainty Factor (CF)** dan **Fuzzy Logic**, yang digunakan untuk membantu pengambilan keputusan berbasis pengetahuan pakar.

Beberapa Tambahan yang berbeda dari modul : 
- Mengubah nilai CF gejala
- Menambahkan 5 Gejala baru
- Perubahan nilai demam menjadi 0,2
- Mengubah input_suhu jadi 22°C
- Menambah Variabel AC 
- Menjelaskan suhu 28°C memiliki nilai keanggotaan di "Nyaman" atau "Panas"
  
Beberapa fitur utama:
- Sistem pakar diagnosis menggunakan metode Certainty Factor.
- Sistem fuzzy logic untuk pengambilan keputusan berdasarkan suhu dan kelembaban.
- Visualisasi grafik fuzzy set.
- Screenshot hasil eksekusi dari masing-masing metode.

📖 **Pengertian Sistem Pakar, Certainty Factor, dan Fuzzy Logic**  
- **Sistem Pakar** adalah program komputer yang meniru cara seorang pakar berpikir dalam menyelesaikan masalah khusus.  
- **Certainty Factor (CF)** digunakan untuk menangani ketidakpastian dalam penalaran berbasis aturan. Setiap aturan diberi nilai keyakinan yang mencerminkan tingkat kepercayaan pakar.  
- **Fuzzy Logic** memungkinkan sistem membuat keputusan berbasis data kabur (tidak pasti), seperti “suhu panas” atau “kelembaban tinggi”, menggunakan derajat keanggotaan.

📂 Sistem-Pakar-CF-Fuzzy/
├── sistem_pakar_cf_fuzzy.py         → Gabungan kode Certainty Factor & Fuzzy Logic
├── hasil_cf_screenshot.png          → Screenshot hasil eksekusi bagian Certainty Factor
├── hasil_fuzzy_screenshot.png       → Screenshot hasil eksekusi bagian Fuzzy Logic
├── README.md                        → Dokumentasi proyek ini

🔧 **Instalasi & Penggunaan (via Google Colab)**
1. **Buka Google Colab**  
   Kunjungi: [https://colab.research.google.com](https://colab.research.google.com)
2. **Unggah file `sistem_pakar_cf_fuzzy.py` ke Colab**  
   - Klik `File > Upload`, lalu pilih file Python kamu.
   - Atau salin langsung isi kodenya ke dalam cell baru.
3. **Install pustaka yang dibutuhkan di Colab:**
   ```python
   !pip install scikit-fuzzy matplotlib
