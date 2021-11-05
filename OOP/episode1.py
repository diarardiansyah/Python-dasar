class mobileLegend(): # <- Template atau class
    pass

namaHero1 = mobileLegend() # <- Object instance
namaHero2 = mobileLegend()

namaHero1.name = "Granger"
namaHero1.role = "Marksman"

namaHero2.name = "Harley"
namaHero2.role = "Mage"

print(namaHero1)
print(namaHero1.__dict__)
print(namaHero2.__dict__)
print(namaHero2.role)