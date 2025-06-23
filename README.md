# Proyek Deteksi Kematangan Manggis

Proyek ini adalah sebuah aplikasi desktop sederhana yang dibuat dengan Python untuk mendeteksi tingkat kematangan buah manggis berdasarkan warna kulitnya dari sebuah gambar. Aplikasi ini menggunakan metode pengolahan citra digital untuk membedakan antara manggis yang matang (berwarna ungu) dan yang belum matang (berwarna hijau).

## Fitur

* **Antarmuka Grafis (GUI)**: Dibangun menggunakan Tkinter untuk kemudahan penggunaan.
* **Upload Gambar**: Pengguna dapat dengan mudah mengunggah gambar buah manggis dari file lokal.
* **Analisis Warna**: Menganalisis gambar dalam ruang warna HSV untuk segmentasi warna yang lebih baik.
* **Segmentasi Gambar**: Menggunakan metode *thresholding* pada *channel Hue* untuk memisahkan area matang dan tidak matang pada buah.
* **Visualisasi Hasil**: Menampilkan gambar asli dan hasil segmentasi secara berdampingan.
* **Histogram Warna**: Menampilkan histogram distribusi warna hijau (belum matang) dan ungu (matang) untuk analisis kuantitatif.

## Cara Kerja

1.  **Konversi Ruang Warna**: Gambar yang diunggah oleh pengguna, yang secara default dalam format BGR, dikonversi ke ruang warna HSV (Hue, Saturation, Value). Ruang warna HSV dipilih karena dapat memisahkan informasi warna (Hue) dari intensitas cahaya, sehingga analisis warna menjadi lebih konsisten dalam berbagai kondisi pencahayaan.
2.  **Thresholding**: Aplikasi ini menerapkan *Otsu's thresholding* pada *channel Hue* dari gambar HSV. Metode ini secara otomatis menentukan nilai ambang batas optimal untuk memisahkan piksel menjadi dua kategori, yang dalam kasus ini adalah:
    * **Area Matang (Putih)**: Piksel yang merepresentasikan warna ungu pada kulit manggis.
    * **Area Belum Matang (Hitam)**: Piksel yang merepresentasikan warna hijau.
3.  **Analisis Histogram**: Untuk memberikan analisis yang lebih detail, program juga menghitung dan menampilkan histogram untuk rentang warna spesifik:
    * **Histogram Hijau**: Menganalisis distribusi *hue* dalam rentang warna hijau (nilai hue 35-85) untuk mengidentifikasi bagian yang belum matang.
    * **Histogram Ungu**: Menganalisis distribusi *hue* dalam rentang warna ungu (nilai hue 120-170) untuk mengidentifikasi bagian yang sudah matang.

## Prasyarat

Sebelum menjalankan aplikasi, pastikan Anda telah menginstal semua pustaka Python yang diperlukan. Berdasarkan file `UAS_PPCD.py`, pustaka yang dibutuhkan adalah:

```bash
pip install opencv-python
pip install numpy
pip install Pillow
pip install matplotlib
```

## Cara Menjalankan

1.  Simpan kode dari repositori ini sebagai file Python (misalnya, `UAS_PPCD.py`).
2.  Buka terminal atau command prompt.
3.  Navigasikan ke direktori tempat Anda menyimpan file tersebut.
4.  Jalankan skrip menggunakan perintah berikut:

    ```bash
    python UAS_PPCD.py
    ```

5.  Jendela aplikasi akan muncul.
6.  Klik tombol **"Upload Foto"** untuk memilih gambar manggis yang ingin dianalisis.
7.  Setelah gambar ditampilkan, klik tombol **"Proses Gambar"** untuk melihat hasil deteksi dan histogramnya.

## Tampilan Aplikasi

Berikut adalah contoh tampilan dari aplikasi saat digunakan:

*(Anda dapat menambahkan screenshot aplikasi di sini untuk memperjelas)*

**Panel Kiri (Gambar Asli)**
![Placeholder untuk Gambar Asli](https://via.placeholder.com/400x300.png?text=Upload+Gambar+Manggis+di+Sini)

**Panel Kanan (Gambar Hasil)**
![Placeholder untuk Gambar Hasil](https://via.placeholder.com/400x300.png?text=Hasil+Segmentasi+Warna)

**Jendela Histogram**
![Placeholder untuk Histogram](https://via.placeholder.com/600x300.png?text=Tampilan+Histogram+Hijau+dan+Ungu)
