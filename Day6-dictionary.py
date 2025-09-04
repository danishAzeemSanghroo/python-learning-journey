map = {"name":"danish","surname":"azeem"}

# for i in map:
#     print(i,map[i])

print("----------------------------------------")
for k,v in map.items():
    print(k,v)
print("----------------------------------------")
print(map["name"])
print("----------------------------------------")
del map["name"]
print(map)
print("----------------------------------------")

print("surname" in map)

print("----------------------------------------")



# Create a dictionary with at least 3 key–value pairs and print it.
dic = {"January":2024,"February":2025,"March":2026}

print(dic)
print("----------------------------------------")
# Access the value of a specific key.
print(dic["February"])
print("----------------------------------------")
# Change the value of an existing key.
dic["February"] = 2028
print(dic["February"])
print("----------------------------------------")
# Add a new key–value pair to the dictionary.
dic["april"] = 2027
print(dic)
print("----------------------------------------")
# Remove a key–value pair using .pop().
dic.pop("april")
print(dic)
print("----------------------------------------")
# Get the list of all keys in the dictionary.
print(dic.keys())
print("----------------------------------------")
# Get the list of all values in the dictionary.
print(dic.values())
print("----------------------------------------")
# Get the list of all key–value pairs using .items().
print(dic.items())
print("----------------------------------------")
# Check if a key exists in a dictionary.
print("March" in dic)
print("----------------------------------------")
# Create a dictionary of 5 students and their marks, then print the student with the highest marks.
students = {"John": 85, "Alice": 92, "Bob": 78, "Emma": 95, "David": 88}
highest = max(students, key=students.get)
print("Top student:", highest, "with marks:", students[highest])

