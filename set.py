a={20,30,'abs',10,20,40}
b={20,30,'abs',10,20,40}
c={20,30,'abs',10,20,40}
print(a is b is c)
print(id(a))
print(id(b))
print(id(c))
a.add(100)
print(a)
d={}
print(type(d))
#it is dictnory