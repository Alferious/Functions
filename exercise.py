#1.Create a function in python thet takes two arguments

def profile(name,age):
    print(name, age)

profile('Alferious', 22)

#2. Create a function with variable length of arguments

def numbers(*values):
    for i in values:
        print(i)

numbers(20,40,60)
numbers(90,78)

#3. Return multiple values from a function

def calculation(a,b):
    sum = a+b
    subtraction = a-b
    return sum,subtraction
        
res = calculation(40,10)
print(res)

#4. Create a function with a default argument
def showEmployee(name,salary = 9000):
    print('Name:',name,'Salary:',salary)
 

showEmployee('Ben',12000)
showEmployee('Jessa')

#5. Create an inner function to calculate the addition in the following way
def numbers(a,b):
    addition = a + b
    sum = addition + 5
    return addition,sum
result = numbers(4,6)
print(result)

#6. Create a recursive function
def addition(num):
    if num:
        return num + addition(num -1)
    else:
        return 0
result = addition(10)
print(result)

#7. Assign a different name to function and call it through the new name
def display_student(name,age):
    print(name,age)

display_student('Emma',26)
show_student = display_student

show_student('Emma',26)

#8. Generate a python list of all even numbers between 4 to 30
print(list(range(4,30,2)))

#9. Find the largest item from a given list

x = [4,6,8,24,12,2]
print(max(x))




    


 


