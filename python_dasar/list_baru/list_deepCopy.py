# Mengambil data dari nested list 
a = [1,2,4,5]
b = [9,0,1,2]

data_list = [a,b]
print(f"Data list {data_list}")

list_2D = data_list[0][2] # <--  0 adalah index pertama dari list 2 dimensi yaitu yg ada di variable a, sedangkan [2] adalah index ke nomor 2 dari data yg ada di variable a
print(f"Data yang ditampilkan adalah = {list_2D}")

# data_2d = [a,b]
# data_copy = data_2d.copy()

# print(f"Address asli = {hex(id(data_2d))}")
# print(f"Address copy = {hex(id(data_copy))}")


# # Menggunakan index member list 
# print(f"Address asli = {hex(id(data_2d[0]))}")
# print(f"Address copy = {hex(id(data_copy[0]))}")

# data_copy[1][0] = 11
# print(f"Data ori  = \n{data_2d}")
# print(f"Data copy = \n{data_copy}")

# Menggunakan deep copy 
'''
    Note = Jika menggunakan nested list dan ingin mengcopy list, gunakan fungsi deepcopy 
'''

from copy import deepcopy

data2D = [a,b]
list_2D_deepcopy = deepcopy(data2D)

print(f"Address data 2D        = {hex(id(data2D))}")
print(f"Address data deep copy = {hex(id(list_2D_deepcopy))}")

# Melihat address berdasarkan member 
print(f"Address asli = {hex(id(data2D[0]))}")
print(f"Address copy = {hex(id(list_2D_deepcopy[0]))}")

list_2D_deepcopy[0][3] = 20
print(f"Data original = \n{data2D}")
print(f"Data list copy setelah diubah menjadi = \n{list_2D_deepcopy}")

# inser list baru di nested list 

list_baru = [0,9,19,1]
list_2D_deepcopy.insert(2, list_baru)
print(f"Data original = \n{data2D}")
print(f"Data list copy setelah diubah menjadi = \n{list_2D_deepcopy}")



