import statistics

inputan = input('Masukkan deret bilangan (pisahkan dengan koma): ')
data = []

for bilangan in inputan.split(','):
    data.append(int(bilangan))

modus = statistics.mode(data)
print(f'Data -> {data}')
print(f'Modus -> {modus}')