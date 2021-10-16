# List lanjutan python

hewan = ['ayam', 'kambing', 'sapi', 'kerbau', 'bebek']
print(hewan)

# Methos menambah data ke dalam list
hewan.append('ikan')
print(hewan)

# Method untuk memisahkan huruf di dalam list
hewan.extend('rusa')
print(hewan)

# Method untuk menginsert data bedasarkan index
hewan.insert(4,'kucing')
print(hewan)

# method untuk menghitung data yg ada pada list
jmlHewan = hewan.count('ayam')
print(f"jumlah data kucing dalam list ada = {jmlHewan}")

# method untuk menghapus data dalam list
hewan.remove('kucing')
print(hewan)

# menghitung panjang list
panjang = len(hewan)
print(panjang)

# method utk membalik data dalam list
hewan.reverse()
print(hewan)

# Menambahkan data ke dalam list dengan variable yg berbeda
print('='*10,"Data list",'='*10)
animal = hewan.copy() # ditambah copy(), agar data pada variable hewan tidak ikut berubah
animal.append('rusa')
print(animal)
print(hewan)

# slicing list
x = hewan[0:7]
print(x)

