# write a program to print MysirG five times on the screen 
# using while loop
i = 1
while i<=5:
    # i = i+1
    i+=1
    print("MySirG")



# program to print first N natural numbers
# while loop 
n = int(input("Enter the number = "))
i = 1
while i<=n:
    print(i, end=" ")
    i+=1


# write a program to calculate sum of first N natural numbers
# using while loop
n = int(input(" Enter the number = "))
i = 1
s = 0
while i<=n:
    s = s+i
    i = i+1
print("sum is = ",s)





# write a program to check wheather a given number is the prime number or not 
# using while loop and break keyword 
n = int(input("Enter a number"))
i = 2
while i<=n-1:
    if n%i == 0:
        break
    i = i+1
if i == n:
    print("PRIME")
else:
    print("NOT PRIME")




# write a program to check wheather a given number is the prime number or not 
# using while loop and break keyword 
n = int(input("Enter a number"))
i = 2
while i<=n-1:
    if n%i == 0:
        print("NOT PRIME")
        break
    i = i+1
else:
    print("PRIME")