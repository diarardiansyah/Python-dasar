# Belajar function return value

# function menghitung akar bilangan kuadrat/ eksponen
def hitung(angka):
    hasil = angka**2
    print(f"hasil dari {angka} adalah = {hasil}")
    return hasil

x = hitung(12)
print(x)

# function double argument
def berhitung(angka1,angka2):
    result = angka1 * angka2
    print(f"hasil dari {angka1} x {angka2} = {result}")
    return (result,"halo haloooo") 

def pengurangan(angka3,angka4):
    hsl = angka3 - angka4
    print(f"hasil dari {angka3} - {angka4} = {hsl}")
    return hsl

y = berhitung(4,pengurangan(50,7))
print(y)


