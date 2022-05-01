l=[10,20,30]
b=bytes(l)
print(type(b))
print(b[0])
print(b[1:2])


l1=[1,2,3,4]
b1=bytearray(l1)
for x in l1:
    print(x)

for x in b1:
    print(b[0])

for x in b1:
    print(b1[1:3])

b1[0]=77
print(b1)
