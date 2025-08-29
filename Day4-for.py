#track monthly expenses

exp = [123,273,292,378,456]
total = exp[0]+exp[1]+exp[2]+exp[3]+exp[4]
print(total)
total = 0
for item in exp:
    total += item
print(total)

#print num 1 to 10

for i in range(1,11):
    print(i*i)

for item in range(len(exp)):
    print(f"Month {item+1} , expense is {exp[item]}")    

key_loc = "chair"
locations = ["window","door","chair","fan"]    

for i in locations:
    if i==key_loc:
        print("Found ", i)
        break
    else:
        print("key not found ",i)


print("----------------------------------")
# Print each character of a string using a for loop.
str = "Danish"
for i in range(len(str)):
    print(str[i])
print("----------------------------------")


# Print only even numbers between 1 and 20.
for i in range(1,21):
    if i%2 ==0:
        print("Even ",i)
    else:
        print("Odd ",i)
print("----------------------------------")
# Print the multiplication table of a number (e.g., table of 5).
for i in range(1,11):
    print(i," x ",5 , " = ", i*5)
print("----------------------------------")
# Count how many vowels are in a string.
str = "Azeem"
vowels = ["a","A","e","E","i","I","o","O","U","u"]
for i in range(len(str)):
    if str[i] in vowels:
        print("Vowel ",str[i]) 
print("----------------------------------")
# Find the largest number in a list using a loop.
num = [123,273,292,378,456,6,3,5]
tem = 0
for i in num:
    if i > tem:
        tem = i
print(f"{tem} is the Greatest num from list {num}")

# Reverse a string using a loop.
str = "danish"
for i in reversed(str):
    print(i)