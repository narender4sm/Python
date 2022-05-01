from sqlite3 import adapt


l=[10,20,30]
print(l)
print(id(l))
l[0]=10000
print(l)
print(id(l))
l1=[10,20,30]
l2=[10000,20,30]
print(id(l1))
print(id(l2))
print(l is l2)

a=[10,20,30]
b=a
print(a)
print(b)
print(id(a))
print(id(b))
a[0]=101
print(a)
print(b)
print(id(a))
print(id(b))
b[1]=201
print(a)
print(b)
print(id(a))
print(id(b))
a1=[30,10,20]
a2=[30,10,20]
print(id(a1))
print(id(a2))
print(a1 is a2)

aa=10
bb=10
print(aa is bb)
print(id(aa))
print(id(bb))

ad=[10,'abc',20,30,40]
print(ad[0])
print(ad[-1])
print(ad[1:4])
ad.append(300)
ad.append(3202)
print(ad)