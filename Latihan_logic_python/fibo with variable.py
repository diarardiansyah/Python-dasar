# mengurutkan fibonacci dengan rekursif

# membuat fungsi fibonacci
def fibo(n):
    if n < 1:
        return [n]
    
    listSebelumN = fibo(n-1)
    angka1 = listSebelumN[-2] if len(listSebelumN) > 2 else 0
    angka2 = listSebelumN[-1] if len(listSebelumN) > 2 else 1

    # print('listSebelumN', listSebelumN)
    # print(f"angka 1 : {angka1}, angka 2 : {angka2}")

    return listSebelumN + [angka1 + angka2]

long = int(input('Masukan panjang deret bilangan : '))

print(fibo(long - 1))

