#~a------> =unary operator -single operation
#a+b--------> binary operator double operation
#a=b if c--->  three operations.
AA=10
BB=20
CC=30 if AA>BB else 40
print(CC)

a=int(input('enter first number:'))
b=int(input('enter second number:'))
min=a if a<b else b
print('the min value:', min)

a1=int(input('enter first number:'))
b1=int(input('enter second number:'))
c1=int(input('enter third number:'))
min=a1 if a1<b1 and a1<c1 else b1 if b1<c1 else c1
print('the min value:', min)

aab=int(input('enter first number:'))
bba=int(input('enter second number:'))
resut=" both equal" if aab==bba else "first is small" if aab<bba else "second bigger"
print(resut)