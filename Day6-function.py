# Write a function that prints "Hello, World!".

def print_hello_world():
    print("Hello, World!")

print_hello_world()

print("--------------------------------------------")

# Write a function that takes a name as input and prints a greeting.
def greeting(name):
    print("Good morning ",name)

greeting("Danish")    

print("--------------------------------------------")

# Write a function that takes two numbers and returns their sum.
def sum(a,b):
    return a+b

print("Sum ",sum(12,12))

print("--------------------------------------------")

# Write a function that returns the square of a number.
def square(a):
    return a*a

print("SQUARE ",square(12))

print("--------------------------------------------")
# Write a function that checks if a number is even or odd.
def check_even_odd(num):
    if num%2==0:
        print(f"Given {num} is Even")
    else:
        print(f"Given {num} is Odd")

check_even_odd(2)        
print("--------------------------------------------")
# Write a function that finds the largest of three numbers.
def find_largest_num(a,b,c):
    if a>b and a>c:
        print(f"{a} is greater than {b} and {c}")
    elif b>a and b>c:
        print(f"{b} is greater than {a} and {c}")
    elif c>a and c>b:
        print(f"{c} is greater than {a} and {b}")
    else:
        print(f"{a} and {b} and {c} are equal")

find_largest_num(1,1,1)
print("--------------------------------------------")
# Write a function that calculates the factorial of a number.
def calculates_factorial(a:any):
    fact = 1
    for i in range(1,a+1):
        fact = fact*i
    return fact
    
print("Factorial ",calculates_factorial(5))   

# Write a function that takes a list of numbers and returns the sum of all numbers.
def sum_of_list(lst:list):
    total = 0
    for i in lst:
        total+=i

    return total

total1 =  sum_of_list([1,2,3])
print("list sum : ",total1)
# Write a function that takes a string and returns it reversed.

def reversed_string(name):
    str = ""
    for i in reversed(name):
        str = str+i
    return str

print("danish | ",reversed_string("danish"))