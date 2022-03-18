sisi = int(input('Masukan sisi = '))

print('Segi tiga sama kaki')


# jumlah = 1
# spasi = int(sisi/2)
# while True:
#     if (jumlah%2):
#         print(" " *spasi,"#"*jumlah)
#         spasi  -= 1
#         jumlah += 1
#     else:
#         jumlah += 1
#         continue

#     if jumlah > sisi:
#         break

for i in range(0, sisi):
    print(" " * (sisi - i), end = "")
    for x in range(i):
        print("# ", end = "")

    print()

for i in range(sisi, 0, -1):
    print(" "*(sisi-i), end='')
    for x in range(i):
        print("# ", end='')
    print()

print('Akhir dari program')


