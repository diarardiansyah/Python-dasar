# Tipe data dictionaty python

clubBola = {"ID" : 1,
            "Nama" : "Manchester United",
            "Markas" : "Old trafford",
            "Julukan" : "The red devils"
        }

clubBola1 = {"ID" : 2,
            "Nama" : "Manchester City",
            "Markas" : "Etihad Stadium",
            "Julukan" : "The Citizen"
        }

listClubBola = {1:clubBola, 2:clubBola1} # <- Mengambil data dictionary berdasarkan ID nya

print(listClubBola[1])
print(listClubBola[2])