def nilai_tengah(deret):
    deret.sort()
    n = len(deret)
    i_tengah = n // 2

    if n % 2 == 1:
        return deret[i_tengah]
    
    return (deret[i_tengah - 1] + deret[i_tengah]) / 2

inputan = input('Masukkan deret bilangan (pisahkan dengan koma): ')
data = []

for bilangan in inputan.split(','):
    data.append(int(bilangan))

print(f'Data -> {data}')
print(f'Median -> {nilai_tengah(data)}')