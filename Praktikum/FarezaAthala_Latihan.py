import numpy as np
from scipy import stats

def hitung_mean(nilai_mahasiswa):
    return round(np.mean(nilai_mahasiswa), 2)

def hitung_median(nilai_mahasiswa):
    return np.median(nilai_mahasiswa)

def hitung_modus(nilai_mahasiswa):
    mode_result = stats.mode(nilai_mahasiswa)
    return int(mode_result.mode)

def hitung_standar_deviasi(nilai_mahasiswa):
    rerata = np.mean(nilai_mahasiswa)
    
    print('\n===== Hitung Rata-Rata =====')
    print(f"rerata = ({' + '.join(map(str, nilai_mahasiswa))}) / {len(nilai_mahasiswa)}")
    print(f'rerata = {rerata:.2f}')

    print('\n====== Hitung Varians =====')
    
    # Verbose Mode
    list_varian = [(bilangan - rerata) ** 2 for bilangan in nilai_mahasiswa]

    for i, item in enumerate(list_varian, start=1):
        print(f'({nilai_mahasiswa[i-1]} - {rerata:.2f}) ^ 2 = {item:.2f}')

    varian = sum(list_varian) / (len(nilai_mahasiswa) - 1)

    rounded_varian_str = [f"{round(value, 2):.2f}" for value in list_varian]
    total_varian_str = ' + '.join(rounded_varian_str)

    print('\ntotal =', total_varian_str)
    print(f'total = {sum(list_varian):.2f}')

    print(f'\nvarian = {sum(list_varian)} / ({len(nilai_mahasiswa) - 1})')
    print(f'varian = {varian:.2f}')

    simpangan_baku = np.sqrt(varian)
    print('\n===== Simpangan Baku =====')
    print('s = akar kuadrat dari varian')
    print(f's = akar kuadrat({varian:.2f})')
    print(f's = {simpangan_baku:.2f}')

    return simpangan_baku

def main():
    nilai_str = input("Masukkan nilai mahasiswa, dipisahkan oleh spasi: ")
    nilai_list = [float(nilai) for nilai in nilai_str.split()]

    print("Pilihan:")
    print("1. rata-rata (Mean)")
    print("2. Nilai Tengah (median)")
    print("3. Modus")
    print("4. Standar Deviasi")

    pilihan = int(input("Masukkan pilihan Anda (1/2/3/4): "))

    if pilihan == 1:
        hasil = hitung_mean(nilai_list)
        print(f"rata-rata (Mean) nilai mahasiswa adalah: {hasil}")
    elif pilihan == 2:
        hasil = hitung_median(nilai_list)
        print(f"Nilai Tengah (median) nilai mahasiswa adalah: {hasil}")
    elif pilihan == 3:
        hasil = hitung_modus(nilai_list)
        print(f"Modus nilai mahasiswa adalah: {hasil}")
    elif pilihan == 4:
        hasil = hitung_standar_deviasi(nilai_list)
        print(f"Standar deviasi nilai mahasiswa adalah: {hasil:.2f}")
    else:
        print("Pilihan tidak valid. Silakan pilih antara 1, 2, 3, atau 4.")

if __name__ == "__main__":
    main()