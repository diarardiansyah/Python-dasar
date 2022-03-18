def buble(A):
    nilai = True
    while nilai:
        nilai = False
        for i in range(len(A) - 1):
            if A[i] > A[i + 1]: # jika index ke 0 lebih besar dari pada index ke 1 maka akan menjalankan statement pertukaran data
                A[i], A[i + 1] = A[i + 1], A[i] # <- Proses pertukaran data 
                nilai = True # <- Jika hasil perbandingan nya True maka akan dilakukan pertukaran 
    return A # <- dan akan mengembalikan nilai A

A = [5, 3, 6, 9, 1]
print(buble(A))