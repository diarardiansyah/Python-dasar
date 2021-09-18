# Latihan konversi temperature

print("\nLatihan konversi temperature suhu\n")

# Fahrenheit
fahrenheit = float(input("Masukan Suhu : "))
print("Suhu diruangan ini adalah :", fahrenheit, "fahrenheit")

# Fahrenheit to Celcius
celcius = ((5/9) * fahrenheit) - 32
print("Suhu diruangan ini adalah :", celcius, "Celcius")

# Celcius to Kelvin
kelvin = (5/9) * (fahrenheit - 32) + 273
print("Suhu di ruangan ini adalah :", kelvin, "kelvin")


print("\nLatihan Konversi temperature suhu\n")

# Kelvin 
kelvin = float(input("Masukan suhu : "))
print("Suhu diruangan ini adalah :", kelvin, "kelvin")

# Kelvin to Celscius 
celcius1 = kelvin - 273
print("Suhu diruangan ini adalah :", celcius1, 'celcius')

# celcius to fahrenheit
fahrenheit1 = (9/5) * (kelvin - 273) + 32
print("Suhu diruangan ini adalah :", fahrenheit1, "fahrenheit")
