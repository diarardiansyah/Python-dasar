class Hero():
    jumlah_hero = 0

    def __init__(self, inputName, inputRole, inputHealth):
        #instance variable
        self.name = inputName
        self.role = inputRole
        self.health = inputHealth
        Hero.jumlah_hero += 1
    
    # void method tanpa argumen dan tanpa return value
    def namaSaya(self):
        print("nama saya adalah = ", self.name)

    # method dengan argumen
    def tambah(self, up):
        self.health += up
        print("bertambah = ")
    
    # method dengan argumen dan return
    def getHealth(self):
        return self.health  


hero1 = Hero("alpha", "fighter", 100)
hero2 = Hero("eudora", "mage", 50)
hero3 = Hero("tigreal", "tank", 200)

'''
print(hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__)
'''

hero1.namaSaya()
hero1.tambah(10)

print(hero1.getHealth())