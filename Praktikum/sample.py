import numpy as np

#Membuat Populasi Data
populasi = np.random.randint(12, 500, 1000)

#Mengambil Sampel Acak
ukuran_sampel = 50
sampel = np.random.choice(populasi, ukuran_sampel, replace=False)

#Menampilkan Sampel
print("Sampel Acak: ", sampel)
