import numpy as np

#Create numpy array
data = np.random.rand(2,3,4,)
zeros = np.zeros((2,2,2))
full = np.full((2,2,2),7)
ones = np.ones((2,2,2))

print(data)
print("-------------------------------------------------------")
print(zeros)
print("-------------------------------------------------------")
print(full)
print("-------------------------------------------------------")
print(ones)

print("-------------------------------------------------------")
#attributes
print(data.shape)
print(data.size)
print(data.dtype)
print("-------------------------------------------------------")


#math operations
list1 = np.random.rand(2)
list2 = np.random.rand(2)

print("sort: ",np.sort(list1))

print("----------------------list1---------------------------------")
print(list1)
print("----------------------list2---------------------------------")
print(list2)
print("----------------------math operations---------------------------------")
print("addition: ", np.add(list1,list2))
print("subtraction: ", np.subtract(list1,list2))
print("multiplication: ", np.multiply(list1,list2))
print("division: ", np.divide(list1,list2))
print("module: ", np.mod(list1,list2))

print("----------------------statistics functions---------------------------------")
print("square: ",np.sqrt(25))
print("power: ",np.power(2,5))
print("absolute value", np.abs(-2))
print("log", np.log(100))
print("exp", np.exp([2,5]))
print("max", np.min(list1))
print("min", np.max(list2))




# arr = np.array([[1,2,4],[4,5,6]])
# print(arr)