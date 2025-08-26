# Take a string input and print it in reverse using slicing.
text = "danish"

# Print the string in reverse using slicing
reversed_text = text[::-1]
print("Reversed string:", reversed_text)

# Convert a string to all uppercase and then to all lowercase.
str = "danIssh"
print(str.upper())
print(str.lower())
# Count how many times a particular letter appears in a string using a built-in string method.
print(str.count("a"))
# Check if a string starts with a given substring.
print(str.startswith("d"))

# Check if a string ends with a given substring.
print(str.endswith("h"))
# Remove leading and trailing spaces from a string.
text = input("Enter a string with spaces: ")
cleaned_text = text.strip()
print("String after removing spaces:", cleaned_text)
print("d a n i s h".strip())
# Replace a specific word in a string with another word using a string method.
text = input("Enter a string: ")
old_word = input("Word to replace: ")
new_word = input("New word: ")
new_text = text.replace(old_word, new_word)
print("Updated string:", new_text)

# Split a sentence into a list of words using the split() method.
sentence = input("Enter a sentence: ")
words = sentence.split()
print("List of words:", words)

# Join a list of words into a single string with spaces in between using the join() method.
list = ["danish",'azeem',"sanghroo"]
sentence = " ".join(list)
print(sentence)
# Find the length of a string using the built-in len() function.
print(len(str))


# Take a string and extract the first 3 characters.
print(text[:3])

# Extract the last 4 characters of a string.
print(text[-4:])

# Get a substring from index 2 to 5.
print(text[2:6])

# Concatenate two strings entered by the user.
a="dan"
b="ish"
print(a+b)

# Repeat a string 3 times using *.
print(a*3)

# Check if a string contains only digits (.isdigit()).
a1 = "125"
print(a1.isdigit()) #true

# Check if a string contains only alphabets (.isalpha()).
str1 = "danish"
print(f"the text '{str1}' , contains only alphabets = {str1.isalpha()} " ) #true

# Check if a string contains both alphabets and numbers (.isalnum()).
alnumStr = 'dan1sh'
print(f" the '{alnumStr}' contains both alphabets and numbers = {alnumStr.isalnum()}")

# Convert the first letter of the string to uppercase (.capitalize()).
print(text.capitalize())

# Convert the first letter of each word to uppercase (.title()).
print(sentence.title())

# Find the index of the first occurrence of a substring (.find()).
x = 'danish'
y = 'ni'
print(f"index of the first occurrence of word {y} a substring =  {x.find(y)}")

# Find the index of the last occurrence of a substring (.rfind()).
x = 'danish'
y = 'ni'
print(f"index of the last occurrence of word {y} a substring =  {x.rfind(y)}")


# Swap the case of all characters (uppercase → lowercase, lowercase → uppercase).
swaptext = 'danisH'
print(swaptext.swapcase())
