import sys

variable1 = [1,2,3,1,3,1,"Saya diar ardiansyah","saya sangat tampan",True,4.4]
variable2 = (1,2,3,1,3,1,"Saya diar ardiansyah","saya sangat tampan",True,4.4) # tuple mengkonsumsi memori lebih sedikit dibandingkan dengan tipe data list

besar_bilangan1 = sys.getsizeof(variable1)
besar_bilangan2 = sys.getsizeof(variable2)

print(f'besar data nya adalah = {besar_bilangan1}')
print(f'besar data nya adalah = {besar_bilangan2}')