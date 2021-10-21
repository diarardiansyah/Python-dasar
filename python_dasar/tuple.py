# Struktur data tuple python 

bilGenap = [2,4,6,8,10,12,14,16]

bilGanjil = (1,3,5,7,9,11,13,15,15,15) # note : tipe data tuple tipe data yang isinya tidak bisa dirubah seperti list, fungsi yang bisa digunakan dlam tipe data tuple hanya index dan count saja

print(type(bilGenap))
print(type(bilGanjil))

manipulate = bilGanjil.index(15)
print(manipulate)
manipulate = bilGanjil.count(15)
print(manipulate)