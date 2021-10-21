# Membuat program mengubah huruf 

huruf = input('Masukan kata pertama : ')
pengganti = input('Masukan kata pengganti : ')

''''
huruf = huruf.replace('a', pengganti)
huruf = huruf.replace('i', pengganti)
huruf = huruf.replace('u', pengganti)
huruf = huruf.replace('e', pengganti)
huruf = huruf.replace('o', pengganti)

print(f'{huruf}')

'''

for huruf1 in 'aiueoAIUEO':
    huruf = huruf.replace(huruf1, pengganti)

print(huruf)