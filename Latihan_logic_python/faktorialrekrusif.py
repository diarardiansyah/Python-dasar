# # Mencari nilai faktorial dengan rekrusif

n = int(input('Masukan nilai faktorial : '))

def nilai_faktorial(n):
    if n > 2:
        return n * nilai_faktorial(n - 1)
    
    return 2

hitung = nilai_faktorial(n) 
print(f"nilai faktorial dari {n} adalah = {hitung:,}")