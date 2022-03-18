# Membuat list dengan range 
data = range(0,15,3) # <-- uruttan 1.Start 2.Stop 3.Step 
print(data) 
list_range = list(data)
print(list_range)

# Membuat list dengan for 
data_list_for = [i for i in range(0,12)] 
print(data_list_for)

# Membuat list dengan for & if
data_list_for_if = [i for i in range(0,11) if i != 7]
print(data_list_for_if)

# Membuat list dengan menampilkan hanya bilangan genap saja 
list_genap = [i for i in range(0,14) if i%2 == 0]
print(list_genap)

# Membuat list dengan menampilkan hanya bilangan ganjil saja
list_ganjil = [i for i in range(0,9) if i%2 != 0]
print(list_ganjil)