# Program tukar isi 2 variable 

a = 'Kambing'
b = 'Sapi'
c = 'Ayam'
d = 'Bebek'

print('===== Hasil Awal =====')
print(f"Binatang A {a}, Binatang B {b}, Binatang C {c}, Binatang D {d} \n")

# pertukaran isi data variable dengan assignment
a,b = b,a 
c,d = d,c
print('===== Hasil Akhir =====')
print(f"Binatang A {a}, Binatang B {b}, Binatang C {c}, Binatang D {d}")
