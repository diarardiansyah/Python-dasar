# Belajar class python
class game():
    #pass  <- pass untuk mengosongkan class
    namaGame = 'nama'

mobileLegend = game() # <- object yang memanggil class
pes = game() # <- object yang memanggil class

# untuk mengubah isi dari object
mobileLegend.namaGame = 'Mobile legend bang bang' 
pes.namaGame = 'Pro evolution soccer'

print(mobileLegend.namaGame)
print(pes.namaGame)