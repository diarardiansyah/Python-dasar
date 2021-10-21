from collections import deque

antri = deque([10,34,56,70,12,33])
print(f'Nilai awal = {antri}')

# menambahkan data ke dalam list
antri.append(100)
print(f'Nilai yang ditambahkan ',100)
print(f'Nilai saat ini = {antri}')

antri.append(113)
print(f'Nilai yang ditambahkan ',113)
print(f'Nilai saat ini = {antri}')

keluar = antri.popleft()
print(f'Nilai yang keluar = {keluar}')
print(f'Nilai saat ini = {antri}')