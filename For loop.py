# for each element present in X sequence(List, set, tuple, dict,string,ranage)

s="Reddy"
for a in s:
    print(a)
    
# print at index

s="ReddyReddy"
b=int(input("enter number"))
for a in s[(b)]:  #S[(b)] index position
    print(a)

# print charachter and index
s="ReddyReddy"
i=0
for x in s:  #S[(b)] index position
    print("The char present at {} index is :{}".format(i,x))
    i=i+1

# renage
for x in range(10):
    print('a')
#print renage number
for x in range(1,10):
    print(x)
#print odd numbers in a range
for x in range(1,21):
    if x%2 != 0:
        print(x)
# print increment values
for x in range(1,21,2):
    print(x)
#decrement values
for x in range(10,-59,-9):
    print(x)

#for loop for list
