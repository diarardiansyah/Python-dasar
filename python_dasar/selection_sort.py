from xml.dom import minicompat

def selection_sort(n):
    for i in range(len(n) - 1):
        min_index = i
        for j in range(i + 1, len(n)):
            if n[min_index] < n[j]:
                min_index = j
        
        # proses pertukaran
        temp = n[i] # <- variable temporary untuk menampung index ke 0 
        n[i] = n[min_index] # <- index ke 0 akan berubah menjadi index ke 4
        n[min_index] = temp # <- index ke 4 akan berubah menjadi index ke 0
    print(f"iterasi", i, n)


def selectionSort(n):
    for i in range(len(n) - 1):
        min_index = i
        for j in range(i + 1, len(n)):
            if n[min_index] > n[j]:
                min_index = j
        
        # Proses pertukaran 
        n[i], n[min_index] = n[min_index], n[i]
    print(f"iterasi", i, n)

n = [4, 2, 7, 10, 1, 90, 100]
print("Cara pertukaran 1")
selection_sort(n)
print("Cara pertukaran 2")
selectionSort(n)