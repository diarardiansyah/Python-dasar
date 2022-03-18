# Mengcopy list 

a = ["Ayam","Merak","Binturong","Harimau","Singa","Sapi"]

print(f"a = {a}")

b = a
print(f"b = {b}")

b[1] = "Buaya"
print(f"Data saat ini menjadi = {a}")
print(f"Data saat ini menjadi = {b}")

# Copy list 
c = a.copy()

# Cara melihat address dari list
print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}")
print(f"address c = {hex(id(c))}")

print(f"Data a = {a}")
print(f"Data b = {b}")
print(f"Data c = {c}")

c[1] = "Jerapah"
print(f"Data setelah diubah menjadi = \n{c}")

c.remove("Singa")
print(f"Data setelah di remove = \n{c}")

# Menghitung dari masing - masing panjang list 
panjang_list_a = len(a)
panjang_list_b = len(b)
panjang_list_c = len(c)
print(f"Panjang list dari a = {panjang_list_a}\nPanjang list dari b = {panjang_list_b}\nPanjang list dari c = {panjang_list_c}")

# Insert list baru 
c.insert(2, "Rusa")
print(f"Data list setelah ditambahkan = {c}")

# Proses pertukaran dua buah variable berisi data list 
d = ["sapi","kerbau"]
e = ["ikan","kodok"]

print(f"Kondisi saat ini {d} & {e}")

d,e = e,d

print(f"Kondisi setelah pertukaran {d} & {e}")