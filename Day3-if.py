#take the number from user and print even or odd
# num = input("Enter any number")
# num = int(num)
num = 2

if num%2==0:
    print(f"the entered number is {num} is even")
else:
    print(f"the entered number is {num} is odd")

# enter dish and check if it contains in list

pakistani_dishes = ["samosa","biryani","karahi","nihari"]

# dish = input("Enter a dish name: ")
dish = "biryani"

if dish in pakistani_dishes:
    print(f"the entered dish '{dish}' is in list: {pakistani_dishes}")
else:
    print(f"entered dish '{dish}' not found")


# Take a number as input and check if it is positive or negative.
num = -1

if num >= 0:
    print(f"the '{num}' is positive")
else:
    print(f"the '{num}' is negative")    

# Take two numbers and print the larger one.
num1 = 12
num2 = 11

if num1>num2:
    print(f" first number '{num1}' is greater than second number '{num2}'")
else:
    print(f" second number '{num2}' is greater than first number '{num1}'")

# Check if a number is divisible by 5.

num = 26

if num%5 == 0:
    print(f"given number '{num}' is divisible by 5")
else:
    print(f"given number '{num}' is not divisible by 5")

# Take a string and check if it contains the word "Python".
str = 'Python1'

if str=='Python':
    print(f"Entered String '{str}' is 'Python'")
else:
    print(f"Entered String '{str}' is not 'Python'")

# Check if a year is a leap year (hint: divisible by 4 but not 100, unless also divisible by 400).

year = 2025

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")

# Take three numbers and print the largest one.
num1 = 12
num2 = 13
num3 = 14

if num1 > num2 and num1>num3:
    print(f"'{num1}' is greater then '{num2}' and '{num3}'")
elif num2 > num1 and num2>num3:    
    print(f"'{num2}' is greater then '{num1}' and '{num3}'")
else:
    print(f"'{num3}' is greater then '{num1}' and '{num2}'")   
 