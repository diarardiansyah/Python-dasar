# memnentukan bilangan prima python

# 1. Membuat fungsi untuk menentukan bilangan prima

def bilPrima(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    
    return True

#inpuBil = int(input("Masukan bilangan prima : "))
#print(bilPrima(inpuBil))

