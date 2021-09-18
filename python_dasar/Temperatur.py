# Program sederhana temprature 

print('\nProgram Konversi Temperature\n')

# Temperature celcius
celcius = float(input("Masukan suhu celcius : "))
print("Suhu di ruangan ini adalah :", celcius, "celcius")

# Temperature reamur 
reamur = (4/5) * celcius
print("Suhu di ruangan ini adalah :", reamur, "reamur")

fahrenheit = ((9/5) * celcius) + 32
print("Suhu di ruangan ini adalah :", fahrenheit, "fahrenhait")

kelvin =  celcius + 273 
print("Suhu di ruangan ini adalah :", kelvin, "kelvin")