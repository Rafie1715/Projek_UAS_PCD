import cv2 as cv
import numpy as np
from tkinter import Tk, Label, Button, filedialog, Frame, LEFT, RIGHT, BOTH, Y
from PIL import Image, ImageTk
from matplotlib import pyplot as plt
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Pastikan menggunakan 'TkAgg' backend untuk Matplotlib
matplotlib.use('TkAgg')

class ManggisDetector:
    def __init__(self, master):
        self.master = master
        master.title("Deteksi Kematangan Manggis")

        # Frame utama
        self.frame_main = Frame(master)
        self.frame_main.pack(padx=20, pady=20, fill=BOTH, expand=True)

        # Frame untuk gambar asli
        self.frame_original = Frame(self.frame_main)
        self.frame_original.pack(side=LEFT, padx=10, pady=10, fill=Y)

        self.label_img_title = Label(self.frame_original, text="Gambar Asli", font=("Helvetica", 14, "bold"))
        self.label_img_title.pack(pady=10)
        
        self.label_img = Label(self.frame_original, borderwidth=2, relief="groove")
        self.label_img.pack()

        self.upload_button = Button(self.frame_original, text="Upload Foto", command=self.upload_image, font=("Helvetica", 12))
        self.upload_button.pack(pady=20)

        # Frame untuk gambar hasil proses
        self.frame_processed = Frame(self.frame_main)
        self.frame_processed.pack(side=RIGHT, padx=10, pady=10, fill=Y)
        
        self.label_result_title = Label(self.frame_processed, text="Gambar Hasil", font=("Helvetica", 14, "bold"))
        self.label_result_title.pack(pady=10)
        
        self.label_result = Label(self.frame_processed, borderwidth=2, relief="groove")
        self.label_result.pack()

        self.process_button = Button(self.frame_processed, text="Proses Gambar", command=self.process_image, font=("Helvetica", 12))
        self.process_button.pack(pady=20)

        # Label untuk keterangan
        self.label_info = Label(self.frame_processed, text="", fg="blue", font=("Helvetica", 10))
        self.label_info.pack(pady=10)

        self.img = None

    def upload_image(self):
        # Membuka dialog file untuk memilih gambar
        file_path = filedialog.askopenfilename()
        if file_path:
            # Membaca gambar menggunakan OpenCV
            self.img = cv.imread(file_path)
            # Menampilkan gambar asli di label
            self.display_image(self.img, self.label_img, width=400, height=300)

    def process_image(self):
        if self.img is not None:
            # Mengkonversi gambar ke ruang warna HSV
            img_hsv = cv.cvtColor(self.img, cv.COLOR_BGR2HSV)
            hue_channel = img_hsv[:,:,0]

            # Lakukan thresholding pada channel hue
            ret, thresh = cv.threshold(hue_channel, 150, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)

            # Menampilkan hasil thresholding di label
            self.display_image(thresh, self.label_result, is_mask=True, width=400, height=300)
            
            # Menambahkan keterangan
            self.label_info.config(text="Warna Putih: Sudah Matang\nWarna Hitam: Belum Matang")
            
            # Hitung histogram dan tampilkan di jendela Matplotlib
            mask_green = cv.inRange(img_hsv, np.array([35, 50, 50]), np.array([85, 255, 255]))
            mask_purple = cv.inRange(img_hsv, np.array([120, 50, 50]), np.array([170, 255, 255]))
            self.display_histogram(img_hsv, mask_green, mask_purple)

    def display_image(self, img, label, is_mask=False, width=None, height=None):
        if is_mask:
            # Mengkonversi mask menjadi gambar PIL
            img = Image.fromarray(img)
        else:
            # Mengkonversi gambar dari BGR ke RGB dan kemudian menjadi gambar PIL
            img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
            img = Image.fromarray(img)

        if width and height:
            # Mengubah ukuran gambar
            img = img.resize((width, height), Image.LANCZOS)

        # Mengonversi gambar PIL ke format yang dapat ditampilkan oleh Tkinter
        img = ImageTk.PhotoImage(img)
        label.configure(image=img)
        label.image = img

    def display_histogram(self, img_hsv, mask_green, mask_purple):
        # Menghitung histogram untuk mask hijau dan ungu
        hist_green = cv.calcHist([img_hsv], [0], mask_green, [180], [0, 180])
        hist_purple = cv.calcHist([img_hsv], [0], mask_purple, [180], [0, 180])

        # Membuat figure dan axes untuk menampilkan histogram
        fig, ax = plt.subplots(1, 2, figsize=(10, 5))

        # Menampilkan histogram hijau
        ax[0].plot(hist_green, color='green')
        ax[0].set_title('Histogram Hijau (Belum Matang)')
        ax[0].set_xlabel('Nilai Hue')
        ax[0].set_ylabel('Frekuensi')
        ax[0].set_xlim([0, 180])

        # Menampilkan histogram ungu
        ax[1].plot(hist_purple, color='purple')
        ax[1].set_title('Histogram Ungu (Sudah Matang)')
        ax[1].set_xlabel('Nilai Hue')
        ax[1].set_ylabel('Frekuensi')
        ax[1].set_xlim([0, 180])

        plt.tight_layout()

        # Menampilkan histogram di jendela terpisah
        fig.canvas.manager.window.attributes('-topmost', 1)
        fig.canvas.manager.window.attributes('-topmost', 0)
        plt.show()

if __name__ == "__main__":
    root = Tk()
    manggis_detector = ManggisDetector(root)
    root.mainloop()
