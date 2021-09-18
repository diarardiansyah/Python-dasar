# Materi comparision

# Object identity is or is not
print('======Materi Object Identity is=======')
y = 7 
t = 1
print('nilai x = ',y, ' ,id =', hex(id(y))) # <-- untuk melihat id dari object 
print('nilai x = ',t, ' ,id =', hex(id(t)))

hasil = y is t
print('y is t adalah = ', hasil)

print('=====Materi Object identity Is Not')
q = 7 
w = 1
print('nilai x = ',q, ' ,id =', hex(id(q)))
print('nilai x = ',w, ' ,id =', hex(id(w)))

hasil = q is not w
print('q is w adalah = ', hasil)


