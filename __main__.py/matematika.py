# Belajar pembuatan modil di python

def perkalian(x,y):
    print('Program sederhana menggunakan fungsi perkalian')
    print(f'{x} x {y} = ',x*y)

def pembagian(x,y):
    print('Program sederhana menggunakan fungsi pembagian')
    print(f'{x} : {y} = ',x / y)

def main():
    print('Ini adalah fungsi main') # <- Fungsi main yang tidak akan muncul jika run program pada file main.py

# membuat pengkondisian jika run program di file matematika maka akan menampilan output __main__
if __name__ == '__main__':
    main()