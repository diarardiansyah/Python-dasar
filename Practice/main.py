from time import process_time_ns

binatang1 = 'Kambing'
binatang2 = 'Rusa'
binatang3 = 'Sapi'
binatang4 = 'Harimau'

print(f"{binatang1}, {binatang2}, {binatang3}, {binatang4}")

binatang1,binatang3 = binatang3,binatang1
binatang2,binatang4 = binatang4,binatang2

print(f"{binatang1}, {binatang3}")
print(f"{binatang2}, {binatang4}")