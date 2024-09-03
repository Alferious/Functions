def my_sum(a,b,c): #my_sum is the function name & (a,b,c) are the parameters
    s = a + b + c
    return s
print('Total is: ',my_sum(30,60,10)) #(30,60,10) are the aguments

#TYPES OF ARGUMENTS
# 1. DEFAULT ARGUMENTS 
# They are assigned default values to the argument using (=) operator
def student(name,age,grade = 'Five',school = 'ABC School'): #grade and school are default arguments
      print('Student Details:',name , age , grade , school)

student('Alferious', 22)

def students(name,age,grade = 'Five', school = 'ABC School'):
     print('Student Details:',name,age,grade,school)

student('Alex', 12 , 'Six') #if you pass values of default arguments while calling a function,then the new values are used instead of the default ones

# 2. KEYWORD ARGUMENTS
#Alter the behaviour of arguments according to their position by assigning the arguments to their name when the function is called

def student(name,age):
     print('Student details:',name,age)

student('Jessa',14) #default function call

student(name = 'John',age = 12) #both keyword arguments

student('Donald', age = 12) #1 positional, 1 keyword

student(age = 13,name = 'Bridget') #changed sequence of keyword arguments

# 3. POSITIONAL ARGUMENTS
#Are arguments where values get assigned to the arguments by their position when the function is called

def add(a,b):
     print(a-b)
add(50,10)

add(10,50)

# KEY TAKE AWAYS ABOUT FUNCTION ARGUMENTS
# 1. Default arguments should follow non-default arguments
# 2. Keyword arguments should follow positional arguments only
# 3. No argument should recieve a value more than once


# 4. ARBITRARY POSITIONAL ARGUMENTS(*ARGS)
#We use variable length arguments if we dont know the number of arguments needed for the function in advance

def percentage(sub1,sub2,sub3):
     avg = (sub1 + sub2 + sub3)/3
     print('Average',avg)

percentage(56,51,73)

def percentage(*subjects):
     sum = 0
     for i in subjects:
          sum = sum + 1

# avg = sum / len(subjects)
# print('Average = ',avg)

# percentage(56,61,73)

#5. ARBITRARY KEYWORD ARGUMENTS(**Kwargs)
#Allows you to pass multiple keyword arguments to a function

def percentage(**kwargs):
     sum = 0
     for sub in kwargs:
          sub_name = sub
          sub_marks = kwargs[sub]
          print(sub_name,'=',sub_marks)
percentage(math=56,english=61,science=73)

