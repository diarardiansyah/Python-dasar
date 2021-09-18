# Operasi artimatika python
a = 20
b = 13

# Operasi pertambahan
print("======Operator Penjumlahan====")
jumlah = a + b
print(a, '+', b, '=', jumlah)

# Operasi Pengurangan
print("======Operator Pengurangan=====")
jumlah = a - b 
print(a, '-', b, '=', jumlah)

# Operasi Perkalian 
print("======Operator Perkalian=====")
jumlah = a * b 
print(a, '*', b, '=', jumlah)

# Operasi Pembagian 
print("======Operator Pembagian=====")
jumlah = a / b
print(a, '/', b, '=', jumlah)

# Operator Modulus
print("======Operator Modulus=====")
jumlah = a % b
print(a, '%', b, '=', jumlah)

# Opearor Floor division
print("======Operator Floor Division=====")
jumlah = a // b
print(a, '//', b, '=', jumlah)

# Operator eksponen
print("======Operator eksponen======")
jumlah = a ** b
print(a, '**', b, '=', jumlah)


'''
    # Opertor yang dijalankan terlebih dahulu
    1. () = tanda kurung
    2. ** = eksponen
    3. Perkalian dan pembagian
    4. Pertambahan dan pengurangan

'''

# Opeator mix
r = 9
t = 6
v = 10

print("======Operator Campuran======")
jumlah = r ** t + v * t - r / v // r % t
print(r, '**', t, '+', v, '*', t, '-', r, '/', v, '//', r, '%', t, '=', jumlah)

jumlah = r + t * v
print(r, '+', t, '*', v, '=', jumlah)
jumlah = (r + t) * v
print('(',r, '+', t, ') *', v, '=', jumlah)



