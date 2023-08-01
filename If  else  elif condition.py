#if cond:
#    sattement1
#    sattement2
#satement3

#comparassion statement
a=1
b=11
if a>b:
    print("A is bigger")
else:
    print("B is bigger")

a=1
b=1
if a==b:
    print("A =B ")
else:
    print("A  not =B ")

#comparassion statement
# with input function

name=input("entername:")
if name=='reddy':
    print ("hello ", name )
print("Hoe are you", name)

#comparassion statement
 
name=input("entername:")
if name=='reddy':
    print ("hello ", name )
else:
    print("You are not ", name)


name=input("entername:")
if name=='reddy':              # it is ture control will here
    print ("hello ", name )
elif name=="narender":          # If above is flase control will here
    print ("hello ", name )
elif name=="malgireddy":        # If above is flase control will here
    print ("hello ", name )
else:                           # If above is flase control will here
    print("You are not ", name)

# no need else statement
name=input("entername:")
if name=='reddy':              # it is ture control will here
    print ("hello ", name )
elif name=="narender":          # If above is flase control will here
    print ("hello ", name )
elif name=="malgireddy":        # If above is flase control will here
    print ("hello ", name )
