# Program kalkulator if dan elif

print("\n"+5*"=" + "Program Calculator Python" +5*"=")

# Inputan angka dari user
angka1 = float(input("Masukan angka pertama : "))
userPilih = input("Masukan operator aritmatika (+,-,x,:) : ")
angka2 = float(input("Masukan angka kedua : "))

# Cek pilihan user
if userPilih == "+":
    hasil = angka1 + angka2
    print(f"Hasil dari perhitungan diatas adalah = {hasil}")
elif userPilih == "-":
    hasil = angka1 - angka2
    print(f"Hasil dari perhitungan diatas adalah = {hasil}")
elif userPilih == "x" or userPilih == "*":
    hasil = angka1 * angka2
    print(f"Hasil dari perhitungan diatas adalah = {hasil}")
elif userPilih == ":" or userPilih == "/":
    hasil = angka1 / angka2
    print(f"Hasil dari perhitungan diatas adalah = {hasil}")
else:
    print(f"Terimakasih sudah mampir di program ini hehehe")


