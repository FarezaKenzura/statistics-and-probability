def hitung_rata_rata_nilai(nilai_mahasiswa):
    jumlah_nilai = sum(nilai_mahasiswa)
    jumlah_mahasiswa = len(nilai_mahasiswa)
    rata_rata = jumlah_nilai / jumlah_mahasiswa
    return rata_rata

# Fungsi Utama
def main():
    # Meminta pengguna untuk memasukkan nilai mahasiswa
    nilai_str = input("Masukkan nilai mahasiswa, dipisahkan oleh spasi: ")
    nilai_list = nilai_str.split()

    #Mengonversi setiap nilai menjadi float
    nilai_mahasiswa = [float(nilai) for nilai in nilai_list]

    # Menghitung Rata rata
    rata_rata = hitung_rata_rata_nilai(nilai_mahasiswa)

    # Menampilkan Rata rata
    print(f"Rata rata nilai mahasiswa adalah: {rata_rata:.2f}")

# Memanggil Fungsi Utama
if __name__ == "__main__":
    main()