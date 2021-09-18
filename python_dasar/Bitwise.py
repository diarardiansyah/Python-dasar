# Belajar operator bitwise

print('=======Operator bitwise python=========')
a = 10
b = 6

# Operator logic OR
c = a | b
print('==========OR=======')
print('nilai : ',a, ' binary : ', format(a, '08b'))
print('nilai : ',b, ' binary : ', format(b, '08b'))
print('===================(|)')
print('hasil dari bitwise diatas adalah :', c, 'binary : ', format(c, '08b'))

# Operator logic AND
c = a & b
print('==========AND=======')
print('nilai : ',a, ' binary : ', format(a, '08b'))
print('nilai : ',b, ' binary : ', format(b, '08b'))
print('===================(&)')
print('hasil dari bitwise diatas adalah :', c, 'binary : ', format(c, '08b'))

# Operator logic XOR
c = a ^ b
print('==========XOR=======')
print('nilai : ',a, ' binary : ', format(a, '08b'))
print('nilai : ',b, ' binary : ', format(b, '08b'))
print('===================(^)')
print('hasil dari bitwise diatas adalah :', c, 'binary : ', format(c, '08b'))

# Operator logic NOT
c = ~a
print('==========NOT=======')
print('nilai : ',a, ' binary : ', format(a, '08b'))
print('===================(~)')
print('hasil dari bitwise diatas adalah :', c, 'binary : ', format(c, '08b'))
print('====================(^)')
d = 0b00001010
e = 0b11111111
print('hasil dari bitwise diatas adalah :', e^d, 'binary :', format(e^d, '08b'))




