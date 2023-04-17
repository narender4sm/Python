#multipule input with comma seperated values
multipuleinput=input("enter numbers:")
print(multipuleinput)
new_inputs=multipuleinput.split(",") #split by comma seperation(",") or also space ()
print(new_inputs)
aa=[int(x) for x in new_inputs]
print(aa)
a,b,c=aa
f=a+b+c
print(f)

#multipule float  input with comma seperated values
float_input=input("enter input:")
print(float_input)
new2_inputs=float_input.split(",")# split float values by comma seperation .spli(",")
print(new2_inputs)
aaa=[float(x) for x in new2_inputs]
print(aaa)
aa,bb,cc=aaa
ff=aa+bb+cc
print(ff)