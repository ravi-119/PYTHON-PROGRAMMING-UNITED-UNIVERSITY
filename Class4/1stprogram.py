# write a program to check whether a given number is positive or non positive
# if condition 
x = int(input("Enter a number"))
if x>0:
    print("number is positive")
if x<0:
    print("number is non-zero/non positive")


# if else condition 
x = int(input("Enter a number"))
if x>0:
    print("number is positive")
else:
    print("number is non-positive/non-zero value")




# if elif else condition 
x = int(input("Enter marks"))
if x>90:
    print("Grade A")
elif x>80:
    print("Grade B")
elif x>70:
    print("Grade C")
elif x>60:
    print("Grade D")
elif x>50:
    print("Grade E")
else:
    print("Grade F")


# single line if else 
# write a program to check wheather a number is even or odd 
# x = int(input("Enter a number"))
print("Even" if int(input("Enter a number"))%2 == 0 else "odd")
