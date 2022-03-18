# Manipulasi list 
list = ["MU","Chelsea","Liverpool","Arsenal"]
data_0 = list[2]
print(data_0)

# Menghitung panjang list 
panjang_list = len(list)
print(f"Panjang list adalah = {panjang_list}")

# Menambahkan data pada list sesuai dengan posisi index
list.insert(2,"Leicester")
print(f"Data saat ini adalah = {list}")

# Menambah list di paling belakang 
list.append("Man city")
print(f"Data list saat ini adalah = {list}")

# Menggabungkan dua buah list
list_kedua = ["Munchen","Real madrid","Barcelona"]
list.extend(list_kedua)
print(f"Data list setelah digabung = {list}")

# Edit data list 
list[2] = "West ham"
print(f"Data list setelah di edit = {list}")

# Remove list 
list.remove("Munchen")
print(f"Data list setelah ada yang di remove = {list}")

# Menghapus list dari belakang
data_belakanag = list.pop()
print(data_belakanag)
print(f"Data saat ini = {list}")