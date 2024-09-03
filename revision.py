def greet(first_name,Last_name):
    print(f'Hi {first_name} {Last_name}')
    print('Welcome aboard')


greet('Alferious','Obonyo')


def greet(name):
    print(f'Hi {name}')

greet('Alferious')


def increment(number,by):
    return number + by

# result = increment(2,1)
# print(result)
print(increment(2,1))

def increment(number,by=1):
    return number + by

print(increment(2,5))


def multiply(x,y):
    return x*y

answer = multiply(2,5)
print(answer)


def multiply(*numbers):
    total = 1
    for number in numbers:
        total = total * number
    return total

print(multiply(2,3,4,5))


def save_user(**user):
    print(user)

save_user(id = 1,name = 'John',age = 22) #prints a dictionary

message = 'a' #global variable

def greet(name):
    message = 'b' #local variable

greet('Alferious')
print(message)


def fizz_buzz(input):
    if (input % 3 ==0) and (input % 5 == 0):
        return 'Fizz_buzz'
    if input % 3 == 0:
        return 'Fizz'
    if input % 5 == 0:
        return "Buzz"
    return input

print(fizz_buzz(6))

