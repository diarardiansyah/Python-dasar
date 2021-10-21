# Menghitung total huruf dengan fungsi yg ada di python

huruf = input('Masukan kata : ').lower() # variable untuk memasukan inputan kata dan jadikan semua huruf lower case
dictionary_huruf_vokal = { # Variable untuk menampung huruf vokal
    'a' : 0,
    'i' : 0,
    'u' : 0,
    'e' : 0,
    'o' : 0
}

for huruf_vokal in dictionary_huruf_vokal.keys():
    dictionary_huruf_vokal[huruf_vokal] = huruf.count(huruf_vokal)

total_vokal = sum(dictionary_huruf_vokal.values()) 

print(f"Total karakter = {len(huruf)}")
print(f"Total huruf vokal = {total_vokal}")
print(f"""
    a -> {dictionary_huruf_vokal['a']}
    i -> {dictionary_huruf_vokal['i']}
    u -> {dictionary_huruf_vokal['u']}
    e -> {dictionary_huruf_vokal['e']}
    o -> {dictionary_huruf_vokal['o']}
""")