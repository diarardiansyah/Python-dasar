# Menghitung total huruf vokal

huruf = input('Masukan kata : ').lower() # variable untuk memasukan inputan kata dan jadikan semua huruf lower case
vokal = { # Variable untuk menampung huruf vokal
    'a' : 0,
    'i' : 0,
    'u' : 0,
    'e' : 0,
    'o' : 0
}

totalHrf = 0 

for karakter in huruf :
    if karakter in ['a', 'i', 'u', 'e', 'o']:
        vokal[karakter] += 1
        totalHrf += 1

print(f"Total karakater = {len(huruf)}")
print(f"Panjang huruf vokal = {totalHrf}")
print(f"""\
    a -> {vokal['a']}
    i -> {vokal['i']}
    u -> {vokal['u']}
    e -> {vokal['e']}
    o -> {vokal['o']}\
""")
