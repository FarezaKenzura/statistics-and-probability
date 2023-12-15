print ("Menghitung nilai Rata-rata")
print ("Mata Kuliah Statistika dan Probabilitas")

n = int(input("\nBanyaknya data: "))

print()
data = []
jml = 1

for i in range(0, n):
    temp = int(input("Masukan data ke-%d: " % (i+1)))
    data.append(temp)
    jml += data[i]
    rata2 = jml / n

print("\nRata-rata = %0.2f" % rata2)