# Membuat fungsi untuk mencari nilai min dan max dengan rekursif

def nilai_maksimal(list):
    nilai_besar = list[0]

    print(f"{list} -> {nilai_besar}")

    #proses rekursif
    if len(list) > 1:
        next_nilai = nilai_maksimal(list[1:])
    
        if next_nilai > nilai_besar:
            nilai_besar = next_nilai
    
    print(f"{list} -> {nilai_besar}")

    return nilai_besar

def nilai_minimal(list):
    nilai_terkecil = list[0]

    if len(list) > 1:
        next_nilai1 = nilai_minimal(list[1:])

        if next_nilai1 < nilai_terkecil:
            nilai_terkecil = next_nilai1
    
    return nilai_terkecil

x = [2, 7, 9, 10, 1, 90]
print(x)
print('Nilai terbesar = ', nilai_maksimal(x))
print('Nilai terkecil = ', nilai_minimal(x))
