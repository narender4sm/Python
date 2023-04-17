# write a program not that year is a leap year if it is divisible by 4 but not by 100 or if it is divisible by 400 (hint: use modulus) //

year = int(input("Enter a year: ")) # ask user for a year
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("{} is a leap year 400".format(year))
        else:
            print("{} is not a leap year 111".format(year))
    else:
        print("{} is a leap year 100".format(year))
else:
    print("{} is not a leap year 4 ".format(year))

