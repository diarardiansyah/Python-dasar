## Belajar python widht and multilane

# Standar
nama = "Diar Ardiasnyah"
umur = 24
tinggi = 173
lahir = "Jakarta"

# Print biodata
biodata = f"nama = {nama}, umur = {umur}, tinggi = {tinggi}, lahir = {lahir}"
print(5*"=" + "Data String" +5*"=")
print(biodata)

# Data miltilane
biodata = f"nama = {nama},\numur = {umur}, \ntinggi = {tinggi}, \nlahir = {lahir}"
print("\n"+5*"=" + "Data String" +5*"=")
print(biodata)

# Menggunakan format kutip tiga
nama = "Diar"
biodata = f"""
nama   = {nama}
umur   = {umur:>5}
tinggi = {tinggi:>5}
lahir  = {lahir}
"""
print("\n"+5*"=" + "Data String" +5*"=")
print(biodata)
