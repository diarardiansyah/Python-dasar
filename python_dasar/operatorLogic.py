# Operator logic boolean

# contoh not 1
a = True
b = not a

print('Maka hasilnya adalah: ',a)
print('======NOT')
print('Maka hasilnya adalah: ',b)

# Opeator or (Jika salah 1 ada yg bernilai true maka outputnya akan true)
print('=======OR========')
b = False
c = False
a = b or c
print('False OR False = ', a)
b = False
c = True
a = b or c
print('False OR True = ', a)
b = True
c = False
a = b or c
print('True OR False = ', a)
b = True
c = True
a = b or c
print('True OR True = ', a)

# Opeator AND (kedua value harus bernilai true jika ingin mendapatkan output true)
print('=========AND===========')
b = False
c = False
a = b and c
print('False AND False = ', a)
b = True
c = False
a = b and c
print('True AND False = ', a)
b = False
c = True
a = b and c
print('False AND True = ', a)
b = True
c = True
a = b and c
print('True AND True = ', a)

# XOR (Salah 1 value harusnya bernilai true jika ingin menghasilkan output true)
print('=====XOR======')
b = False
c = False
a = b ^ c
print('False XOR False = ', a)
b = True
c = False
a = b ^ c
print('True XOR False = ', a)
b = False
c = True
a = b ^ c
print('False XOR True = ', a)
b = True
c = True
a = b ^ c
print('True XOR True = ', a)

