# Menggunakan __init__ / constructor

from os import name

class mobileLegend():

    # class variabel 
    jml_hero = 0

    def __init__(self, inputName, inputRole, inputHealth):
        self.name = inputName
        self.role = inputRole
        self.health = inputHealth
        mobileLegend.jml_hero += 1
        print(f"Membuat hero mobile legend {inputName}")
    
namaHero1 = mobileLegend("Granger", "Marksman", 10)
print(mobileLegend.jml_hero)
namaHero2 = mobileLegend("Karrie", "Marksman", 15)
print(mobileLegend.jml_hero)
namaHero3 = mobileLegend("Balmond", "Fighter", 50)
print(mobileLegend.jml_hero)

'''
print("==== Nama hero mobile legend ====\n")
print(namaHero1.__dict__)
print(namaHero2.__dict__)
print(namaHero3.__dict__)
'''