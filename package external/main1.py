from PIL import Image

foto = Image.open("jastok.jpg")

print("Format file :" + foto.format)
print("Ukuran file :" + str(foto.size))
print("Tinggi foto :" + str(foto.height))

foto.show()