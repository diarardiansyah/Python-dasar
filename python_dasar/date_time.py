# Date time python

import datetime as dt

hari_ini = dt.date.today()
print(f"Hari ini hari = {hari_ini:%A}")

## menampilkan tanggal, bulan dan tahun lahir
print("Silahkan masukan tanggal lahir, \nbulan dan tahun anda")
tanggal = int(input("Masukan tanggal lahir anda \t: "))
bulan = int(input("Masukan bulan lahir anda \t: "))
tahun = int(input("Masukan tahun lahir anda \t: "))

lahir = dt.date(tahun,bulan,tanggal)
print(f"Tanggal bulan dan tahun lahir anda adalah {lahir}")

## menghitung umur sesuai tahun lahir
today = dt.date.today()
umur_hari = today - lahir
umur_tahun = umur_hari.days // 365
umur_bulan = (umur_hari.days % 365) // 30
print(f"Hari nya adalah hari = {lahir:%A}")
print(f"Umur anda adalah = {umur_tahun} tahun, {umur_bulan} bulan")


