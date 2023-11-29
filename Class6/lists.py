#Hetrogenous elements
#list1 that is employeelist   
employee = [" Ravi verma", "Rahul parajapati", "puskar singh", "Glen maxwell","Prabhans tiwari", "Priyanshu singh", "Ayushi singh" ]
print(employee)
print(employee[0])
print(employee[1], employee[3])
print(employee[-2])



# # Accessing list elements via whilw loop
i = 0 
while i <= 3:
    print(employee[i], end=" ")
    i = i+1


# # Accessing list elements via for loop
for x in employee:
    print(x, end="")

employee.append("Mitchell starc")
print(employee)
del employee

# # how to delete element of list
del employee[1]
print(employee)

# # How to edit an element of llist 
print(employee)
employee [1] = "gyaan"
print(employee)

# How to append an element of an list
employee.append("Sachin")
print(employee)
 
# How to insert an element of an list 
employee.insert(2, "ram")
print(employee)


# Unpacking
l1 = [20,30,40,50]
print(l1)

# Packing
a = 5
b = 6
c = 10
l2 = [a,b,c]
print(l2)


# Built in Methods 
print(len(l1))
print(len(l2))
print(max(l2))
print(min(l2))
print(sum(l2))
print(sorted(l2))


# list() Method 
l1 = list()
l1 = list(10)
l1 = list(10,20,30)
l1  = list([10,20,30])
l1 = list("mysirg")
l1 = list(range(5))
print(l1)




# Comparison operator on list
l1 = [1,2,3]
l2 = [2,3,1]
l3 = [1,2,3,4,5]
l4 = [1,2,3]

print(l1 == l2)
print(l1 == l3)
print(l1 == l4)
print(l1 > l2)





# Concatination operator 
l1 = [1,5,9]
l2 = [2,3,1]
l3 = l1 + l2
print(l3)
l1 += l2
l1 = l1 + l2
print(l1)

# Repetition operator
l1 = [2,5]
result = l1*5
print(result)
print(l1)




# list of lists
l4 = [ [1,3,5], [2,1,8], [5,4,4] ]
print(l4[0]) 
print(l4[1])
print(l4[2])
print(l4[0] [0])
print(l4[2] [2])
print(l4.f1())


# list object methods 
l5 = [1, 10, 28, 90, 75, 86, 89, 20, 20, 90]
print(l5)
l5.append("Ravi")
print(l5)
l5.insert(3,"Aman")
print(l5)
l5.remove(10)
print(l5)
x = l5.pop()
print(x)
x = l5.pop()
print(x)
# l5.clear()
print(l5)
l5.reverse()
print(l5)
print(l5.index("Aman"))
print(l5)
print(l5.count(90))
print(l5.count(20))
print(l5.count(100))
print(sorted(l5))
l5.sort()
print(l5)

# sorted 
l12 = [70, 40, 90, 35, 45, 20, 50]
print(l12)

# accending order
print(sorted(l12))

# decending order
print(sorted(l12, reverse=True))

l12.sort()
print(l12)



# List Comprehension 
l6 = [a+1 for a in range(5)]
print(l6)

l9 = [3+4 for a in range(5)]
print(l9)

l10 = [a**2 for a in range(2, 10, 2)]
print(l10)

oddnumbers = [2*e-1 for e in range(1,int(input("Enter a number"))+1)]
print(oddnumbers)