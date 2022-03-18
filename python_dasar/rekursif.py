def factorial(n):
    if n == 1:  
        return n # <- Jika hasil faktorial adalah 1 maka akan dikembalikan nilai 1
    else:
        return n * factorial(n - 1)

print(factorial(5))


# factorial while 
def factorialWhile(n):
    nilai = 1
    while n > 0:
        nilai = nilai * n
        n = n - 1
    return nilai

print(factorialWhile(5))

# 3. bilangan fibonaci
def fibonaci(n):
    if n == 1:
        return [1]
    elif n == 0:
        return [0]
    else:
        return fibonaci(n - 1) + [n]
    
print(fibonaci(11))

