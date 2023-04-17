#and or not are logical oparators
#and returns if both arguments are True.

from ast import Not


print(True and True)#True
print(True and False)#False
print(False and False)#False
print(False and True)#False

# or = atleat one argument should be true and it returns True.

print(True or True)#True
print(True or False)#True
print(False or False)#flase
print(False or True)#true

#not not true
not True
not False

#logical operator for non boolean type
#x and y
#if X evaluates to Flase then the result is X
#If X evaluates to true then the result is Y
print(10 and 1) # 10 is non zero=True then the result is y=1
print(10 and 20) #10 is non zero=True the the result y=20
print(0 and 20) # 0 is False the the resulti is x=0


# or operator for non boolean values.
#if X evaluates to Flase then the result is Y
#If X evaluates to true then the result is X
print(10 or 1) # 10 is non zero=True then the result is X=10
print(0 or 20) # 0 is False the the resulti is Y
print('ab' or 10) # ab= non zero= true and result is ab
print([] or 'ab') # [] empty list is 0 and result is ab
print('' or 'ab') #'' empty string is o and the result is ab

# not function for non boolan fuction
print(not 'abc') # abdc=1=non zero=true and opposite is false.
print(not 0) # 0=flase answer is opposite is True
print(not 1) # 1=True answer is oppsite is False
print(not 10)# 10=1=non zero=true and opposite is false.
print(not '') # ''=empty strin=0=flase answer is opposite is True
print(not [])# []=empty list=0=flase answer is opposite is True