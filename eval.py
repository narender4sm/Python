#eval function
a=input("enter anything:")  # default value will be string
a1=eval(input("enter anything")) #10.5 takes as float
a2=eval(input("enter anything")) #True takes as bool
a3=eval(input("enter anything")) #10 takes as int
a4=eval(input("enter anything")) #[10,20,30] takes as list
a5=eval(input("enter anything")) #(10,20) or (10,) takes as tuple
print(type(a))
print(type(a1))
print(type(a2))
print(type(a3))
print(type(a4))
a6=eval(input("enter")) # print the sum
print(a6)
