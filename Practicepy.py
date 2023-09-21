# gives fruits list with price
fruits=["Apple","Banana","Dragon fruit"]
prices=[10,20,30,100,55]
fruits_list1=("Grapes","mango")
#Fruit list extended
fruits.extend(fruits_list1)
print(fruits)
for x in fruits,prices:
  print(fruits[x],prices[x])  