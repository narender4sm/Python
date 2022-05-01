a=10000000
b=10000000
c=20
print(id(a))
print(id(b))
print(id(c))
d=100000.01
e=100000.01
print(id(d))
print(id(e))
print(a is b)
print(d is e)
f=True
g=True
print(id(f))
print(id(g))
print(f is g)
h=10+20j
i=10+20j
print(id(h))
print(id(i))
print(h is i)