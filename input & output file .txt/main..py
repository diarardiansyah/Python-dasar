# Membuat input dan output file .txt menggunakan python 

'''
1. w = write mode digunakan untuk menulis dan menghapus file lama, jika file tidak ada maka akan dibuat file baru
2. r = rad mode hanya bisa digunakan untuk membaca file 
3. a = append digunakan untuk menambah data pada file .txt
4. r+ = write and read mode
'''

tulisan = open('index.txt', 'w')

tulisan.write('Contoh program membuat file input dan output menggunakan bahasa pemrograman python')
tulisan.write('\nContoh program kedua dari diar ardiansyah')
tulisan.write('\nDiar ardiansyah sangat ganteng sekali')

tulisan.close()

# fungsi read hanya bisa digunakan untuk melihat saja
tulisan1 = open('index.txt', 'r')

#print(tulisan1.read()) # <- contoh jika hanya ingin mengambil spesifik berapa karakter

print(tulisan1.readline())

# Menggunakan fungsi append

tulisan3 = open('index.txt','a')

tulisan3.write('\nDiar ardiansyah manusai yang sangat keren dan ganteng di muka bumi wk')

tulisan3.close()
