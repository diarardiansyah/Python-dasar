# List 2 dimensi 
a = [1,3,4,5]
b = [1,7,8,1]
c = [0,8,8,1]

list_2D = [a,b,c]
print(f"List 2 dimensi = {list_2D}")

# Pengunaan nested list
binatang1 = ["Gajah",5,"Jantan"]
binatang2 = ["Jerapah",7,"Betina"]
binatang3 = ["Harimau",8,"Jantan"]

data_binatang = [binatang1,binatang2,binatang3]
print(f"Data binatang = {data_binatang}\n")

for binatang in data_binatang:
    print(f"Nama hewan\t = {binatang[0]}") 
    print(f"Usia hewan\t = {binatang[1]}")
    print(f"Gender    \t = {binatang[2]}\n")




