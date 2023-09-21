#tuple () unchangeble
t=(10,20,30,10,20)
# print type
print(type(t))
#prints index position
print(t[0])
print(t[-1])
#prints indelex list
print(t[0:3])
#print the lentgth of tuple
print(len(t))
#no append
#no adding
#no removal
t1=()
print(type(t1))
print(len(t1))
# if item exists in tuples print output
fruits = ("apple", "banana", "cherry")
if "apple" in fruits:
    print("Apple exists in fruits")
# tuple values can't be changed
#type casting tuple into lists and into tuple
fruits_list=list(fruits)
print(fruits_list)
print(type(fruits_list))
fruits_list1=tuple(fruits_list)
print(type(fruits_list1))
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
    print(thistuple[i])


