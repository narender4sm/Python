# print using while loop
i=3
while i<=10:
    print ("hello while loop", i)
    i=i+1

# print number between 1 to 20 divisiblw by 3
i=1
while i<=20:
    if i%3==0:
        print ("the number divisible by 3 is ", i)
    i=i+1

# sum of given numbers
n=int(input('Enter the number: '))
sum=0
i=1
while i<=n:
    sum=sum+i
    i=i+1
print(" The sum is : ", sum)