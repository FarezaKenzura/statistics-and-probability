import scipy.stats as stats

# Data Sampel
data1 = [70, 75, 85, 90, 100]
data2 = [80, 85, 88, 95, 99]
data3 = [75, 80, 82, 88, 95]

#Melakukan ANOVA one-way
fvalue, pvalue = stats.f_oneway(data1, data2, data3)

#Menampilkan hasil
print("Nilai F: ", fvalue)
print("Nilai P: ", pvalue)