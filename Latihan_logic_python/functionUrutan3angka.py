# Membuat function dari urutan 3 angka 

# fungsi untuk melihat angka yang terbesar
def angka_besar(h,i,j):
    if h > i and h > j :
        return h
    elif i > h and i > j:
        return i
    elif h == i and h == j :
        return(h,i,j)
    
    return j

def angka_kecil(h,i,j):
    if h < i and h < j :
        return h
    elif i < h and i < j:
        return i
    elif h == i and h == j :
        return(h,i,j)
    
    return j
    
def angka_tengah(h,i,j):
    if(h > i and h < j) or (h < i and h > j):
        return h
    elif(i > h and i < j) or (i < h and i > j):
        return i
    
    return j

# Menginput inputan user 
h = int(input('Masukan angka 1 : '))
i = int(input('Masukan angka 2 : '))
j = int(input('Masukan angka 3 : '))

a1 = angka_kecil(h, i, j)
a2 = angka_tengah(h, i, j)
a3 = angka_besar(h, i, j)

print(f"urutan angka = {a1}, {a2}, {a3}")