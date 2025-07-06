# 🚦 TrafficSync AI – Dual-Line Vehicle Counter

**TrafficSync AI** adalah sistem deteksi dan penghitungan kendaraan berbasis YOLOv8 yang menghitung jumlah mobil berdasarkan area sentuhan terhadap dua garis horizontal pada video. Proyek ini memanfaatkan model YOLOv8 hasil training custom untuk mengenali objek `cars` dan menghitung jumlah mobil berdasarkan **lokasi spesifik dalam frame video**.

---

## 📌 Fitur Utama

- 🎯 Deteksi kendaraan (mobil) secara real-time dari video menggunakan YOLOv8.
- 📏 Menggambar **dua garis horizontal terpisah** di frame:
  - **Garis kiri** di 78% tinggi layar
  - **Garis kanan** di 60% tinggi layar
- 🔴 Menghitung **mobil saat titik pusat (titik merah) dari bounding box menyentuh garis** (dengan toleransi)
- 🔄 Sistem tracking ID sederhana agar mobil tidak dihitung ganda
- 📊 Menampilkan dua counter:
  - `Left Count` (untuk garis kiri)
  - `Right Count` (untuk garis kanan)

---

## 📷 Contoh Hasil

![TrafficSync Detection Sample](assets/screenshot.png)  
*Gambar: Deteksi mobil menyentuh garis hijau (kiri) dan garis merah (kanan), counter ditampilkan di pojok kiri atas.*

> 📎 *Kamu bisa ganti link gambar dengan path screenshot kamu setelah upload, misalnya `assets/output.png`.*

---

## 🚀 Cara Kerja

1. Model YOLOv8 (`best.pt`) mendeteksi mobil per frame.
2. Titik tengah (center) dari setiap mobil dihitung.
3. Jika titik tengah mobil **menyentuh garis horizontal kiri/kanan**, maka:
   - Mobil dihitung sekali saja (per ID)
   - Count diperbarui sesuai lokasi garis
4. Hasil ditampilkan secara real-time dalam jendela OpenCV.

---

## 🛠️ Teknologi yang Digunakan

| Komponen       | Teknologi             |
|----------------|------------------------|
| Deteksi Objek  | [YOLOv8 - Ultralytics](https://docs.ultralytics.com/) |
| Pengolahan Video | OpenCV                |
| Model Custom   | `best.pt`  hasil training pribadi |
| Bahasa         | Python 3               |

---

## 📁 Struktur Proyek


---

## 🧠 Kegunaan Proyek Ini

- 🚦 **Simulasi sistem monitoring lalu lintas** berbasis AI
- 🧪 **Validasi analitik kendaraan** di jalur/jurusan berbeda
- 📉 **Pengumpulan data kendaraan** untuk studi kepadatan/arus lalu lintas
- 🏙️ Potensi integrasi ke **Smart City** & sistem **manajemen lampu lalu lintas cerdas**

---

## ✅ Hasil yang Diperoleh

- Hitung kendaraan berdasarkan **area yang ditentukan**
- Tampilkan hasil langsung secara visual
- Dapat disesuaikan ke arah kiri/kanan, atas/bawah, atau bahkan zona tertentu

---

## 👨‍💻 Kontributor

> 🎓 Proyek ini dikembangkan untuk eksplorasi AI & Computer Vision  
> 🔧 Developer: **Darrell Dzaky Ahnaf**  
> 💡 Framework: YOLOv8 + OpenCV + Python

---

## 📜 Lisensi

Proyek ini menggunakan lisensi bebas untuk eksplorasi akademik dan non-komersial.  
Untuk penggunaan komersial, silakan ajukan permohonan terlebih dahulu.





---

## 🧠 Kegunaan Proyek Ini

- 🚦 **Simulasi sistem monitoring lalu lintas** berbasis AI
- 🧪 **Validasi analitik kendaraan** di jalur/jurusan berbeda
- 📉 **Pengumpulan data kendaraan** untuk studi kepadatan/arus lalu lintas
- 🏙️ Potensi integrasi ke **Smart City** & sistem **manajemen lampu lalu lintas cerdas**

---

## ✅ Hasil yang Diperoleh

- Hitung kendaraan berdasarkan **area yang ditentukan**
- Tampilkan hasil langsung secara visual
- Dapat disesuaikan ke arah kiri/kanan, atas/bawah, atau bahkan zona tertentu

---

## 👨‍💻 Kontributor

> 🎓 Proyek ini dikembangkan untuk eksplorasi AI & Computer Vision  
> 🔧 Developer: **Darrell Dzaky Ahnaf**  
> 💡 Framework: YOLOv8 + OpenCV + Python

---

## 📜 Lisensi

Proyek ini menggunakan lisensi bebas untuk eksplorasi akademik dan non-komersial.  
Untuk penggunaan komersial, silakan ajukan permohonan terlebih dahulu.

---


