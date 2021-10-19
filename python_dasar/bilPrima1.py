# mencari bil prima dengan range angka

# Fungsi untuk menentukan suatu bilangan masuk ke bilangan prima atau bukan 
def bilPrima(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    
    return True

# fungsi untuk mencari bilangan prima dengan range angka
def cariBilangan(angka1, angka2):
    listBil = [] # berfungsi untuk menanmpung angka bilangan prima jika bernilai True

    for x in range(angka1, angka2 + 1):
        if bilPrima(x): # untuk mengecek apakah bilangan tsb bilangan prima jika iya akan dimasukan ke dlm list
            listBil.append(x) # untuk menambah bilangan prima tsb ke dalam list
    
    return listBil

inputan = int(input("Masukan angka 1 : "))
inputan2 = int(input("Masukan angka 2 : "))
print(cariBilangan(inputan, inputan2))
