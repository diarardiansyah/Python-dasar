# menghitung nilai faktorial dengan looping for

# masukan inputan user untuk angka yang dimasukan
n = int(input('Masukan nilai faktorial : '))
fak = 1 # variable angka awal untuk nilai faktorial 

for i in range(2, n + 1): 
    fak *= i

print(f"nilai faktorial dari {n} adalah = {fak}")