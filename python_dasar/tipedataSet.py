# Belajar tipe data set python

# note : type data set tidak berlaku output data yang berurutan dalam tipe ini output urutan data bisa tidak sesuai dengan apa data yang diinputkan
'''
set1 = {"sepak bola","basket","badminton","renang"}

tambah = set1.add("lompat indah")
tambah = set1.add("lari")
tambah = set1.add("renang") # jika memasukan data yang sama dengan data existing pada tipe data set hanya menampilkan output 1 data saja yang sudah ada, berbeda dengan list
print(set1)

'''
sepakBola = set()

sepakBola.add("Manchester United")
sepakBola.add("Manchester City")
sepakBola.add("Chelsea")
sepakBola.add("Liverpool")
sepakBola.add(28)

print(sepakBola)

hewan = {"harimau", "rusa", "bekantan"}
hewan1 = {"chetah", "binturong", "orang utan"}
number = {"ikan", "chetah", "orang utan"}

print(hewan.union(hewan1)) # <- proses menggabungkan 1 variabel dengan variabel yang lainnnyaæ
print(hewan1)
print(hewan1.intersection(number)) # <- jika menggunakan fungsi ini, bilamana ada value yang sama diantara 2 var tersebut maka hanya akan menampilkan data yang value nya sama saja, jika value nya tidak sama data tidak ditampilkan

