# fibonacci non rekursif

# 1. Menggunakan metode list

# memasukan inputan user untuk panjang deret
x = int(input('Masukan panjang deret : '))

fibo = [0, 1]

for i in range(2, x):
    #index1 = i - 2
    #index2 = i - 1
    #print(f"deret fibonacci {(i + 1)} adalah index - {index1} + index - {index2}")
    angka1 = fibo[i - 2]
    angka2 = fibo[i - 1]
    hasilAngka = angka1 + angka2

    fibo.append(hasilAngka)

print(fibo)
