# Belajar python dasar stacks

stacks = [10,20,30,40,50,60]
print(f'Nilai awal {stacks}')

# memasukan data ke dalam list
stacks.append(70)
print(f'data yang masuk = ',70)
print(f'data saat ini = {stacks}')

stacks.append(100)
print(f'data yang masuk = ',100)
print(f'data saat ini = {stacks}')

# mengeluarkan data dari dalam list
keluar = stacks.pop()
print(f'data yang keluar = {keluar}')
print(f'data saat ini = {stacks}')